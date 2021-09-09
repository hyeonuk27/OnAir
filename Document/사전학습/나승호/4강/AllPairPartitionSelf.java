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

public class AllPairPartitionSelf {
	public static class MapClass1 extends Mapper<Object, Text, Text, Text> { 

                private String Tablename;
		private int numberOfPartitions = 2; // number of partition
		private Text emitkey = new Text();

		public void setup(Context context) throws IOException {
			Configuration configuration = context.getConfiguration();
			Tablename = configuration.get("Tablename", "r");
			numberOfPartitions = configuration.getInt("numberOfPartitions", 2);
		}

		// Text : input line
		// --> format = <Relation id> \tab <record id> \tab <dimension 1> \tab
		// <dimension 2>

		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {
			
			String[] tuple = value.toString().split( "\t" );
			
			int recordId = Integer.parseInt(tuple[1]);
			int partitionId = recordId % numberOfPartitions;
			
			for( int i = 0; i < numberOfPartitions; i++ ) {
				String text = "";
				if (tuple[0].equals(Tablename)) {
					if (i <= partitionId) {
						emitkey.set("(" + i + "," + partitionId + ")");
					}
					else {
						emitkey.set("(" + partitionId + "," + i + ")");
					}
					context.write(emitkey, value);
				}
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
			String s = new String();
			for (Text val: values) {
				s += ("\n" + val.toString());
			}
			emitval.set(s);
			context.write(key, emitval);
		}
	}

	public static void main(String[] args) throws IOException,
			InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args)
				.getRemainingArgs();
		if (otherArgs.length != 4) {
			System.out.println("usage:  <Tablename> <numberOfPartition> <in> <out>");
			System.exit(1);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[3]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);


                Job job = new Job(conf, "allpair-partition-self");
                Configuration config = job.getConfiguration();
                config.set("Tablename", otherArgs[0]);
                config.setInt("numberOfPartitions", Integer.parseInt(otherArgs[1]));
		job.setJarByClass(AllPairPartitionSelf.class);
		job.setNumReduceTasks(2);
		job.setMapperClass(MapClass1.class);
		job.setReducerClass(ReduceClass1.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[2]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[3]));
		if (!job.waitForCompletion(true))
			System.exit(1);
	}
}
