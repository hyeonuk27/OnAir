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

public class AllPairPartition {
	public static class MapClass1 extends Mapper<Object, Text, Text, Text> { 

                private String Table1name;
                private String Table2name;
		private int numberOfPartitions = 2; // number of partition

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

		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {
			
			String[] tuple = value.toString().split( "\t" );
			
			Random rn = new Random();
			int partitionId = rn.nextInt( numberOfPartitions );
			
			for( int i = 0; i < numberOfPartitions; i++ ) {
				
                        	// TODO
                        	// ------------------------------------------------------
				//
                        	// ------------------------------------------------------
			}

		}
	}

	public static class ReduceClass1 extends Reducer<Text, Text, Text, Text> {

		private Text emitval = new Text();

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();
		}

		public void reduce(Text key, Iterable<Text> values, Context context)
				throws IOException, InterruptedException {

                       	// TODO
                       	// ------------------------------------------------------
			//
                       	// ------------------------------------------------------
		}
	}

	public static void main(String[] args) throws IOException,
			InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args)
				.getRemainingArgs();

		if (otherArgs.length != 5) {
			System.out.println("usage:  <Table1name> <Table2name> <numberOfPartition> <in> <out>");
			System.exit(1);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[4]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

                Configuration config = job.getConfiguration();
                config.set("Table1name", otherArgs[0]);
                config.set("Table2name", otherArgs[1]);
                config.setInt("numberOfPartitions", Integer.parseInt(otherArgs[2]));
		Job job = new Job(conf, "allpair-partition");
		job.setJarByClass(AllPairPartition.class);
		job.setNumReduceTasks(1);
		job.setMapperClass(MapClass1.class);
		job.setReducerClass(ReduceClass1.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[3]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[4]));
		if (!job.waitForCompletion(true))
			System.exit(1);
	}
}
