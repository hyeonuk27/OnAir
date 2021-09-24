package ssafy;

import java.io.*;
import java.util.*;
import java.lang.Math;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.compress.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.*;

public class CommonItemCount {

	/*
	 * Map class part
	 */

	public static class InvertedIndexMapper extends Mapper<Object, Text, Text, Text> {

		private Text rid = new Text();
		private Text item = new Text ();

		// Text : input line
		// --> format = <rid \t item item item ...>
		public void map (Object key, Text value, Context context) throws IOException, InterruptedException
		{
			StringTokenizer itr = new StringTokenizer( value.toString() );

			// get record id
			String id = itr.nextToken();
			rid.set(id);
			
			// emit < [item], [rid] > pairs for each item in the record
                        while (its.hasMoreTokens()){
                        	item.set(itr.nextToken());
                        	context.write(item, rid);
                        }
		}
	}

	/*
	 * Reduce class part
	 */

        public static class InvertedIndexReducer extends Reducer<Text, Text, Text, IntWritable> {

		private Text ridpair = new Text();
                private static IntWritable one = new IntWritable(1);

                // input: < item, [rid1, ..., ridn] >
                public void reduce(Text key, Iterable<Text> values, Context context)
                        throws IOException, InterruptedException
                {
                        // read the value list
                        Vector<String> str = new Vector<String>();
                        for ( Text val : values ) {
                                str.add( val.toString() );
                        }

                        // emit < [ridi ridj], 1 > for every pair
                        for (int i=0; i<str.size(); i++){
                        	for (int j=i+1; j<str.size();j++){
                        		if (str.get(i).compareTo(str.get(j)) < 0)
                        			ridpair.set(str.get(i) + "" + str.get(j));
                			else
                				ridpair.set(str.get(j) + "" + str.get(i));
					context.write(ridpair, one);
                        	}
                        }
                }
        }


	public static class SimMapper extends Mapper<Object, Text, Text, IntWritable> {

		private Text ridpair = new Text();
		private IntWritable count = new IntWritable();
		
		public void map( Object key, Text value, Context context ) throws IOException, InterruptedException {

                        // emit < [ridi ridj], 1 > for every pair
                        StringTokenizer itr = new StringTokenizer( value.toString());
                        ridpair.set(itr.nextToken()+""+itr.nextToken());
                        count.set(Integer.parseInt(itr.nextToken());
                        context.write(ridpair, count);

		}
	}

	public static class SimReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

		private Text ridpair = new Text();
		private IntWritable count = new IntWritable();

		public void reduce( Text key, Iterable<IntWritable> values, Context context ) throws IOException, InterruptedException {
			
                        // emit < [ridi ridj], count > for every pair
                        int overlap = 0;
                        for (IntWritable val : values) {
                        	overlap += val.get();
                        }
                        StringTokenizer itr = new StringTokenizer( key.toString() );
                        ridpair.set("(" + itr.nextToken() + "," + itr.nextToken() +  ")");
                        count.set( overlap );
			 context.write( ridpair, count );
			context.write(ridpair , count );
		}
	}

	public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration ();
		FileSystem fs = FileSystem.get( conf );
    	String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 3) {
			System.out.println ("usage: <in> <out1> <out2>");
			System.exit(2);
		}

		// run phase1 job
		Job job1 = new Job (conf, "buildSetInvertedIndex");
		job1.setJarByClass(CommonItemCount.class);
		job1.setMapperClass(InvertedIndexMapper.class);
		job1.setReducerClass(InvertedIndexReducer.class);
		job1.setOutputKeyClass(Text.class);
		job1.setOutputValueClass(Text.class);
		job1.setNumReduceTasks(2);
            	FileInputFormat.addInputPath(job1, new Path(otherArgs[0]));
		Path pathtmp = new Path( otherArgs[1] );
                FileOutputFormat.setOutputPath(job1, pathtmp );
                if ( fs.exists( pathtmp ) ) 
			fs.delete( pathtmp );
		if ( !job1.waitForCompletion( true ) ) 
			System.exit(1);


                Job job2 = new Job( conf, "DistinctPairCount" );
                job2.setJarByClass( CommonItemCount.class );
                job2.setMapperClass( SimMapper.class );
                job2.setReducerClass( SimReducer.class );
                job2.setOutputKeyClass( Text.class );
                job2.setOutputValueClass( IntWritable.class );
                FileInputFormat.addInputPath( job2, new Path( otherArgs[1] ) );
                FileOutputFormat.setOutputPath( job2, new Path( otherArgs[2] ) );
		if ( fs.exists( new Path( otherArgs[2] ) ) ) 
			fs.delete( new Path( otherArgs[2] ) );
                if ( !job2.waitForCompletion( true ) ) 
			System.exit(1);

	}
}

