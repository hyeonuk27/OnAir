package ssafy;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MatrixMulti1 {
	// Map
	public static class MMMapper extends Mapper<Object, Text, Text, Text>{
		private Text keypair = new Text();	// 
		private Text valpair= new Text();	//
                private String Matrix1name;
                private String Matrix2name;
		private int n;	// 
		private int m;  //	
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
		public void map(Object key, Text value, Context context
				) throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}
	// Reduce
	public static class MMReducer extends Reducer<Text, Text, Text, IntWritable> {
		private IntWritable val = new IntWritable();	// emit할 value로 사용할 변수
		private int l;	// matrix A의 행

		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

		}
		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException {
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}
	// Main
        public static void main(String[] args) throws Exception {
                Configuration conf = new Configuration();
                String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
                if (otherArgs.length != 7) {
                        System.err.println("Usage: <Matrix 1 name> <Matrix 2 name> <Number of rows in Matrix 1><Number of columns in Matrix 1 (i.e., Number of rows in Matrix 2)> <Number of columns in Matrix 2> <in> <out>");
                        System.exit(2);
                }

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[6]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

                Job job = new Job(conf, "1-phase matrix multiplication");
                Configuration config = job.getConfiguration();
                config.set("Matrix1name", otherArgs[0]);
                config.set("Matrix2name", otherArgs[1]);
                config.setInt("n",Integer.parseInt(otherArgs[2]));
                config.setInt("l",Integer.parseInt(otherArgs[3]));
                config.setInt("m",Integer.parseInt(otherArgs[4]));

                job.setJarByClass(MatrixMulti1.class);
                job.setMapperClass(MMMapper.class);
                job.setReducerClass(MMReducer.class);
                job.setMapOutputKeyClass(Text.class);
                job.setMapOutputValueClass(Text.class);
                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(IntWritable.class);
                job.setNumReduceTasks(2);

                FileInputFormat.addInputPath(job, new Path(otherArgs[5]));
                FileOutputFormat.setOutputPath(job, new Path(otherArgs[6]));
                if (!job.waitForCompletion(true))
                        System.exit(1);
        }
}

