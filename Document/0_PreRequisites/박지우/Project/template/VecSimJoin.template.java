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

public class VecSimJoin {

	/*
	 * Map class part
	 */

	public static class MapClass1 extends Mapper<Object, Text, Text, Text> {

		private int numberOfPartitions = 4;

		private Text emitkey = new Text ();
		private Text emitval = new Text ();

                public void setup(Context context) throws IOException {
                        Configuration configuration = context.getConfiguration();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
                }


		// Text : input line
		// --> format = <point id> \tab <dimension 1> \tab <dimension 2>
		public void map (Object key, Text value, Context context) throws IOException, InterruptedException
		{
			// emit key-value pairs
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}


	/*
	 * Reduce class part
	 */


	public static class ReduceClass1 extends Reducer<Text, Text, Text, Text> {

		private int numberOfPartitions = 4;
		private float threshold;

		private Text emitkey = new Text ();
		private Text emitval = new Text ();


		public void setup (Reducer.Context context)
		{
                        Configuration configuration = context.getConfiguration();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}

		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException
		{

			Vector <String> vecs1 = new Vector <String> ();
			Vector <String> vecs2 = new Vector <String> ();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
			vecs1.clear ();
			vecs2.clear ();
		}


        	public static double dist(String sp1, String sp2) {
                	// parse string
                	String[] strarr1 = sp1.split("\t");
                	String[] strarr2 = sp2.split("\t");
                	//System.out.print("dist function start: strarr.length=");
                	double d1, d2, diff, sum = 0;
                	for (int i = 1; i < strarr1.length; i++) {
                        	d1 = Double.parseDouble(strarr1[i]);
                        	d2 = Double.parseDouble(strarr2[i]);
                        	diff = d1 - d2;
                        	sum += diff * diff;
                	}
                	return Math.sqrt(sum);
        	}


	}

	public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration ();
    	String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 4) {
			System.out.println ("usage: <numberOfPartitions> <threshold> <in> <out>");
			System.exit(1);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output1 = new Path(otherArgs[3]);
                if (hdfs.exists(output1))
                        hdfs.delete(output1, true);

		conf.setInt ("numberOfPartitions", Integer.parseInt(otherArgs[0]));
		conf.setFloat ("threshold", (float)Double.parseDouble(otherArgs[1]));

		Job job = new Job (conf, "bruteforce");
		job.setJarByClass(VecSimJoin.class);

		job.setNumReduceTasks (2);

		job.setMapperClass(MapClass1.class);
		job.setReducerClass(ReduceClass1.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		FileInputFormat.addInputPath(job, new Path(otherArgs[2]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[3]));

		if (! job.waitForCompletion(true))
			System.exit (1);
	}
}

