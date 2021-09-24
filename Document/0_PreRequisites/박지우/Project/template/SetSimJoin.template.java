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

public class SetSimJoin {

	/*
	 * Map class part
	 */

	public static class InvertedListMapper extends Mapper<Object, Text, Text, Text> {

		private Text rid = new Text();
		private Text item = new Text ();

		// Text : input line
		// --> format = <p \t item item item ...>
		public void map (Object key, Text value, Context context) throws IOException, InterruptedException
		{

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

		}
	}

	/*
	 * Reduce class part
	 */

	public static class InvertedListReducer extends Reducer<Text, Text, Text, IntWritable> {

		private static IntWritable one = new IntWritable(1);

		// input: < item, [p:p.size, ..., q:q.size] >
		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException
		{
			// read the value list
			Vector<String> str = new Vector<String>();
			for ( Text val : values ) {
				str.add( val.toString() );
			}


                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class SimMapper extends Mapper<Object, Text, Text, IntWritable> {

		private Text pair = new Text();
		private IntWritable count = new IntWritable();
		
		public void map( Object key, Text value, Context context ) throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class SimReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

		private static double sigma;

		protected void setup( Context context ) throws IOException, InterruptedException {

			Configuration config = context.getConfiguration();
			sigma = config.getFloat( "threshold", -1 );
		}
		
		public void reduce( Text key, Iterable<IntWritable> values, Context context ) throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

		}
	}

	public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration ();
		FileSystem fs = FileSystem.get( conf );
    	String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 3) {
			System.out.println ("usage: <threshold> <in> <out>");
			System.exit(2);
		}
		conf.setFloat ("threshold", (float)Double.parseDouble(otherArgs[0]));

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[2]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

		// run phase1 job
		Job job1 = new Job (conf, "buildInvertedList");
		job1.setJarByClass(SetSimJoin.class);
		job1.setMapperClass(InvertedListMapper.class);
		job1.setReducerClass(InvertedListReducer.class);
		job1.setOutputKeyClass(Text.class);
		job1.setOutputValueClass(Text.class);
		job1.setNumReduceTasks(2);
		FileInputFormat.addInputPath(job1, new Path(otherArgs[1]));
		Path pathtmp = new Path( "setSimJoinTmp" );
		FileOutputFormat.setOutputPath(job1, pathtmp );
		if ( fs.exists( pathtmp ) ) fs.delete( pathtmp );
		if ( !job1.waitForCompletion( true ) ) System.exit(1);

		// Run phase2 job
                // TODO
                // ------------------------------------------------------
                 //
                // ------------------------------------------------------


	}
}

