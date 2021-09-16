package ssafy;

import java.io.*;
import java.util.*;
import java.sql.*;
import java.lang.Math;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.compress.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

//import org.apache.hadoop.util.*;

public class TopKSearch {

        public static class MyType implements Comparable<MyType> {
                public MyType(double d, String s) {
                        dist = d;
                        str = s;
                }

                public double dist;
                public String str;

                @Override
                public int compareTo(MyType o) {
                        return this.dist > o.dist ? -1 : (this.dist < o.dist ? 1 : 0);
                }
        }


	/*
	 * Map class part
	 */

	public static class MapClass1 extends Mapper<Object, Text, Text, Text> {

		private int numOfPartitions = 4;

		private Text emitkey = new Text ();
		private Text emitval = new Text ();

		public void setup (Mapper.Context context)
		{
			Configuration conf = context.getConfiguration ();
			numOfPartitions = conf.getInt ("numberOfPartitions", 2);

		}

		// Text : input line
		// --> format = <point id> \tab <dimension 1> \tab <dimension 2>
		public void map (Object key, Text value, Context context) throws IOException, InterruptedException
		{
			String arr[] = value.toString().split ("\t", 2);

			// read record ID from a line
			int rid = Integer.parseInt (arr[0]);

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

		private int numOfPartitions = 4;
		private int K;
		private String query;

		private Text emitkey = new Text ();
		private Text emitval = new Text ();

		public void setup (Reducer.Context context)
		{
			Configuration conf = context.getConfiguration ();
			numOfPartitions = conf.getInt ("numberOfPartitions", 2);
			K = conf.getInt ("K", 2);
			query =  conf.get ("queryPoint", "");

		}

		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException
		{

			String[] keyarr = key.toString().split ("\t");
			double d;
                        PriorityQueue<MyType> queue = new PriorityQueue<MyType>();
                        // Find the Top-K closest points from the query point.
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------


		}


	        public static double dist(String sp1, String sp2) {
                	// parse string
                	String[] strarr1 = sp1.split("\t");
                	String[] strarr2 = sp2.split("\t");
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


	public static class MapClass2 extends Mapper<Object, Text, Text, Text> {
		private Text emitkey = new Text("dummy");
		private Text emitval = new Text();

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class ReduceClass2 extends Reducer<Text, Text, Text, Text> {

		private int K;
		public void setup (Reducer.Context context)
		{
			Configuration conf = context.getConfiguration ();
			K = conf.getInt ("K", 2);

		}
		private Text emitkey = new Text();
		private Text emitval = new Text();

		public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
			PriorityQueue<MyType> queue = new PriorityQueue<MyType>();
                        // Find the Top-K closest points from the query point.
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------


		}
	}

	public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration ();
    		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 6) {
			System.out.println ("usage: <numberOfPartitions> <queryPoint> <K> <in> <out1> <out2>");
			System.exit(1);
		}

                // To broadcast the parameters to map and reduce
                conf.setInt("numberOfPartitions", Integer.parseInt(otherArgs[0]));
		String arr[] = otherArgs[1].split (":");
		String query = "0";
		for (int i = 0; i < arr.length; i++)
			query = query + "\t" + arr[i];
                conf.set("queryPoint", query);
                conf.setInt("K", Integer.parseInt(otherArgs[2]));


                FileSystem hdfs = FileSystem.get(conf);
                Path output1 = new Path(otherArgs[4]);
		Path output2 = new Path(otherArgs[5]);
                if (hdfs.exists(output1))
                        hdfs.delete(output1, true);
		if (hdfs.exists(output2))
			hdfs.delete(output2, true);


		Job job = new Job (conf, "1st phase");
		job.setJarByClass(TopKSearch.class);
		job.setNumReduceTasks (2);
		job.setMapperClass(MapClass1.class);
		job.setReducerClass(ReduceClass1.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[3]));
		FileOutputFormat.setOutputPath(job, output1);
		if (! job.waitForCompletion(true))
			System.exit (1);


                // Fill here for the second phase
                // TODO
                // ------------------------------------------------------
                //
                // ------------------------------------------------------
	}
}

