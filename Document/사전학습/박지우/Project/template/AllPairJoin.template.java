package ssafy;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

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

public class AllPairJoin {
	public static class MapClass1 extends Mapper<Object, Text, Text, Text> {

		private String Table1name; 
		private String Table2name;
		private int JoinAttr1 = 1; // join attribute
		private int JoinAttr2 = 1; // join attribute
		private int numberOfPartition = 2; // number of partition

		private Text emitkey = new Text();
		private Text emitval = new Text();

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
		// if the join attribute is dimension1, joinatt = 2
		// relatation id => 0, record id => 1, dimension 1 => 2, dimension 2 =>
		// 3

		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {
			
			String[] tuple = value.toString().split( "\t" );
			
			Random rn = new Random();
			int partitionId = rn.nextInt( numberOfPartition );
			

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	public static class ReduceClass1 extends Reducer<Text, Text, Text, Text> {

		private ArrayList<String> r; // array for storing records of R
		private ArrayList<String> s; // array for storing records of S
		private Text emitkey = new Text();
		private Text emitval = new Text();
		
		private String Table1name; 
		private String Table2name;
		private int JoinAttr1 = 0; // join attribute
		private int JoinAttr2 = 0; // join attribute

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}

		public void reduce(Text key, Iterable<Text> values, Context context)
				throws IOException, InterruptedException {
			r = new ArrayList<String>();
			s = new ArrayList<String>();
			

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------


			r.clear();
			s.clear();
		}
	}

	public static void main(String[] args) throws IOException,
			InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args)
				.getRemainingArgs();
		if (otherArgs.length != 7) {
			System.out.println("usage: <Table1name> <Table2name> <JoinAttr1> <JoinAttr2> <NumPartition> <in> <out>");
			System.exit(1);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[6]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

                Job job = new Job(conf, "repartition-join");
                Configuration config = job.getConfiguration();
                config.set("Table1name", otherArgs[0]);
                config.set("Table2name", otherArgs[1]);
                config.setInt("JoinAttr1", Integer.parseInt(otherArgs[2]));
                config.setInt("JoinAttr2", Integer.parseInt(otherArgs[3]));
                config.setInt("NumPartition", Integer.parseInt(otherArgs[4]));

		job.setJarByClass(AllPairJoin.class);
		job.setNumReduceTasks(2);
		job.setMapperClass(MapClass1.class);
		job.setReducerClass(ReduceClass1.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[5]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[6]));
		if (!job.waitForCompletion(true))
			System.exit(1);
	}
}
