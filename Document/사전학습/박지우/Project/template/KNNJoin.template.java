package ssafy;

import java.io.IOException;
import java.util.Random;
import java.util.*;
import java.lang.Math;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class KNNJoin {
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

	public static class MapClass1 extends Mapper<Object, Text, Text, Text> {
                private String Table1name;
                private String Table2name;
                private int numberOfPartitions = 2; // number of partition
		private Text emitkey = new Text();

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
		// Text : input line
		// --> format = <Relation id> \tab <record id> \tab <dimension 1> \tab
		// <dimension 2>
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			String[] tuple = value.toString().split("\t");
			Random rn = new Random();
			int partitionId = rn.nextInt(numberOfPartitions);

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class ReduceClass1 extends Reducer<Text, Text, Text, Text> {

                private String Table1name;
                private String Table2name;
		private Text emitkey = new Text();
		private Text emitval = new Text();
		private int K;

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}

		public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

			Vector<String> vecs1 = new Vector<String>();
			Vector<String> vecs2 = new Vector<String>();

                        // TODO
                        // ------------------------------------------------------
                        //


			vecs1.clear();
			vecs2.clear();
		}
	}

	public static class MapClass2 extends Mapper<Object, Text, Text, Text> {
		private Text emitkey = new Text();
		private Text emitval = new Text();

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class ReduceClass2 extends Reducer<Text, Text, Text, Text> {
		private Text emitval = new Text();
		private int K;

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();
			K = configuration.getInt("K", 2);
		}


		public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

		}
	}

	public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 7) {
			System.out.println("usage:  <Table1name> <Table2name>  <numberOfPartitions> <K> <in> <out1> <out2>");
			System.exit(1);
		}
		FileSystem hdfs = FileSystem.get(conf);
		Path output1 = new Path(otherArgs[5]);
		Path output2 = new Path(otherArgs[6]);
		if (hdfs.exists(output1))
			hdfs.delete(output1, true);
		if (hdfs.exists(output2))
			hdfs.delete(output2, true);

                // Phase 1
		Job job1 = new Job(conf, "allpair-knn1");
                Configuration config1 = job1.getConfiguration();
                config1.set("Table1name", otherArgs[0]);
                config1.set("Table2name", otherArgs[1]);
		config1.setInt("numberOfPartitions", Integer.parseInt(otherArgs[2]));
		config1.setInt("K", Integer.parseInt(otherArgs[3]));

		job1.setJarByClass(KNNJoin.class);
		job1.setNumReduceTasks(2);
		job1.setMapperClass(MapClass1.class);
		job1.setReducerClass(ReduceClass1.class);
		job1.setOutputKeyClass(Text.class);
		job1.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job1, new Path(otherArgs[4]));
		FileOutputFormat.setOutputPath(job1, output1);
		if (!job1.waitForCompletion(true))
			System.exit(1);
		// Phase 2
                // TODO
                // ------------------------------------------------------
                //
                // ------------------------------------------------------

	}
}
