package ssafy;

import java.io.IOException;
import java.util.*;
import java.lang.Math;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
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

public class LabelRatio{

	public static class TokenizerMapper 
	extends Mapper<Object, Text, Text, IntWritable>{

		public void map(Object key, Text value, Context context
		) throws IOException, InterruptedException {
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

			}
		}
	}

	public static class IntSumReducer 
	extends Reducer<Text,IntWritable,Text,IntWritable> {

		public void reduce(Text key, Iterable<IntWritable> values, 
				Context context
		) throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}


        // phase2 Map
        public static class M2Mapper extends Mapper<Object, Text, Text, Text>{   

                public void map(Object key, Text value, Context context)
                        throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

			}
                }
        }
        // phase2 Reduce
        public static class M2Reducer extends Reducer<Text,Text,Text,Text> {

                public void reduce(Text key, Iterable<Text> values, Context context)
                        throws IOException, InterruptedException {

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
                }
        }

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 3) {
			System.err.println("Usage: <in> <out1> <out2>");
			System.exit(2);
		}
                Path output1 = new Path (otherArgs[1]);
                if (FileSystem.get(conf).exists(output1)) {
                        FileSystem.get(conf).delete (output1);
                }

		Job job = new Job(conf, "label ratio");
		job.setJarByClass(LabelRatio.class);
		job.setMapperClass(TokenizerMapper.class);
		job.setCombinerClass(IntSumReducer.class);
		job.setReducerClass(IntSumReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

                job.setNumReduceTasks(1);
		FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
		job.waitForCompletion(true);


                // TODO
                // ------------------------------------------------------
                //
                // ------------------------------------------------------

	}
}
