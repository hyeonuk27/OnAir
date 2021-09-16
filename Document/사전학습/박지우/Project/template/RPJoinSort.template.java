package ssafy;

import java.io.*;
import java.util.*;


import java.lang.Math;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.*;


public class RPJoinSort {
	   public static class MapClass1 extends Mapper<Object, Text, IntPair, Text> {
		 	private int joinatt = 0;	// join attribute
			private IntPair emitkey = new IntPair ();
			private Text emitval = new Text ();

			public void setup(Context context) throws IOException {
				Configuration configuration = context.getConfiguration();
				joinatt = configuration.getInt("joinatt",0);
			}
			// Text : input line
			// --> format = <Relation id> \tab <record id> \tab <dimension 1> \tab <dimension 2>
			// if the join attribute is dimension1, joinatt = 2
			// relatation id => 0, record id => 1, dimension 1 => 2, dimension 2 => 3
			public void map (Object key, Text value, Context context) throws IOException, InterruptedException
			{
				// TO DO

				context.write(emitkey, value);
				
			}
	   }
	   public static class ReduceClass1 extends Reducer<IntPair, Text, Text, Text> {
	 	    private ArrayList<String> r;	// array for storing records of R
			private Text emitkey = new Text ();
			private Text emitval = new Text ();

			public void setup(Context context) throws IOException {
			}

			public void reduce(IntPair key, Iterable<Text> values, Context context) throws IOException, InterruptedException{


			}
		}

	   	public static class IntPair implements WritableComparable<IntPair> {
		private int first = 0;
		private int second = 0;
	
		/**
		 * Set the left and right values.
		 */
		public void set(int left, int right) {
			first = left;
			second = right;
		}
		
		public String toString()
		{
			return Integer.toString(first) + "\t" + Integer.toString(second);
		}
		
		public int getFirst() {
			return first;
		}
		public int getSecond() {
			return second;
		}
		/**
		 * Read the two integers. 
		 * Encoded as: MIN_VALUE -> 0, 0 -> -MIN_VALUE, MAX_VALUE-> -1
		 */
		@Override
		public void readFields(DataInput in) throws IOException {
			first = in.readInt() + Integer.MIN_VALUE;
			second = in.readInt() + Integer.MIN_VALUE;
		}
		@Override
		public void write(DataOutput out) throws IOException {
			out.writeInt(first - Integer.MIN_VALUE);
			out.writeInt(second - Integer.MIN_VALUE);
		}
		@Override
		public int hashCode() {
			return first * 157 + second;
		}
		@Override
		public boolean equals(Object right) {
			if (right instanceof IntPair) {
				IntPair r = (IntPair) right;
				return r.first == first && r.second == second;
			} else {
				return false;
			}
		}
		/** A Comparator that compares serialized IntPair. */ 
		public static class Comparator extends WritableComparator {
			public Comparator() {
				super(IntPair.class);
			}
	
			public int compare(byte[] b1, int s1, int l1,
					byte[] b2, int s2, int l2) {
				return compareBytes(b1, s1, l1, b2, s2, l2);
			}
		}
	
		static {                                        // register this comparator
			WritableComparator.define(IntPair.class, new Comparator());
		}
	
		@Override
		public int compareTo(IntPair o) {
			if (first != o.first) {
				return first < o.first ? -1 : 1;
			} else if (second != o.second) {
				return second < o.second ? -1 : 1;
			} else {
				return 0;
			}
		}
	}

		/**
		   * Compare only the first part of the pair, so that reduce is called once
		   * for each value of the first part.
		   */
	   	public static class FirstGroupingComparator 
	   	implements RawComparator<IntPair> {
	   		@Override
	   		public int compare(byte[] b1, int s1, int l1, byte[] b2, int s2, int l2) {
	   			return WritableComparator.compareBytes(b1, s1, Integer.SIZE/8, 
	   					b2, s2, Integer.SIZE/8);
	   		}

	   		@Override
	   		public int compare(IntPair o1, IntPair o2) {
	   			int l = o1.getFirst();
	   			int r = o2.getFirst();
	   			return l == r ? 0 : (l < r ? -1 : 1);
	   		}
	   	}

	   	public static class FirstPartitioner extends Partitioner<IntPair, Text>{
	   		@Override
	   		public int getPartition(IntPair key, Text value, 
	   				int numPartitions) {
	   			return Math.abs(key.getFirst() * 127) % numPartitions;
	   		}
	   	}

		public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
			Configuration conf = new Configuration ();
	    	String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
			if (otherArgs.length != 3) {
				System.out.println ("usage: <joinatt> <in> <out>");
				System.exit(1);
			}

                	FileSystem hdfs = FileSystem.get(conf);
                	Path output = new Path(otherArgs[2]);
                	if (hdfs.exists(output))
                        	hdfs.delete(output, true);

			conf.setInt ("joinatt", Integer.parseInt(otherArgs[0]));
			Job job = new Job (conf, "repartition-join");
			job.setJarByClass(RPJoinSort.class);
			job.setNumReduceTasks (1);
			job.setMapperClass(MapClass1.class);
			job.setReducerClass(ReduceClass1.class);
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(Text.class);
			job.setMapOutputKeyClass(IntPair.class);
			job.setMapOutputValueClass(Text.class);
			FileInputFormat.addInputPath(job, new Path(otherArgs[1]));
			FileOutputFormat.setOutputPath(job, new Path(otherArgs[2]));
			job.setPartitionerClass(FirstPartitioner.class);
			job.setGroupingComparatorClass(FirstGroupingComparator.class);
			if (! job.waitForCompletion(true))
				System.exit (1);
			}
}

