package ssafy;

import java.io.*;
import java.util.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MatrixMulti3 {

	public static class IntTriple implements WritableComparable {
		private int v1;
		private int v2;
		private int v3;

		public IntTriple () {}

		public IntTriple (int v1, int v2, int v3) { set(v1, v2, v3); }

		public void set (int v1, int v2, int v3) { this.v1 = v1; this.v2 = v2; this.v3 = v3;}

		public int getV1 () { return this.v1; }
		public int getV2 () { return this.v2; }
		public int getV3 () { return this.v3; }

		public void readFields(DataInput in) throws IOException
		{
			v1 = in.readInt();
			v2 = in.readInt();
			v3 = in.readInt();
		}

		public void write(DataOutput out) throws IOException
		{
			out.writeInt(v1);
			out.writeInt(v2);
			out.writeInt(v3);
		}

		public int hashCode ()
		{
			int a = v1 * 3571 + v2 * 13781 % 6301 + v3;
			a = (a+0x7ed55d16) + (a<<12);
			a = (a^0xc761c23c) ^ (a>>19);
			a = (a+0x165667b1) + (a<<5);
			a = (a+0xd3a2646c) ^ (a<<9);
			a = (a+0xfd7046c5) + (a<<3);
			a = (a^0xb55a4f09) ^ (a>>16);
			return a;
		}

		public boolean equals(Object o) 	{
			if (!(o instanceof IntTriple)) return false;
			IntTriple other = (IntTriple)o;
			return (this.v1 == other.v1 && this.v2 == other.v2 && this.v3 == other.v3);
		}

		public int compareTo(Object o)	{
			IntTriple other = (IntTriple)o;

			if (v1 < other.v1) return -1;
			else if (v1 > other.v1) return 1;
			else {
				if (v2 < other.v2) return -1;
				else if (v2 > other.v2) return 1;
				else {
					if (v3 < other.v3) return -1;
					else if (v3 > other.v3) return 1;
					else return 0;
				}
			}
		}

		public String toString()
		{
			return Integer.toString(v1) + "\t" + Integer.toString(v2) + "\t" + Integer.toString(v3);
		}

		public static class Comparator extends WritableComparator {
			public Comparator() { super(IntTriple.class); }
			public int compare(byte[] b1, int s1, int l1, byte[] b2, int s2, int l2) {
				int thisv1 = readInt(b1, s1);
				int thisv2 = readInt(b1, s1 + 4);
				int thisv3 = readInt(b1, s1 + 8);
				int thatv1 = readInt(b2, s2);
				int thatv2 = readInt(b2, s2 + 4);
				int thatv3 = readInt(b2, s2 + 8);

				if (thisv1 < thatv1)  return -1;
				else if (thisv1 > thatv1)  return 1;
				else {
					if (thisv2 < thatv2)  return -1;
					else if (thisv2 > thatv2)   return 1;
					else {
						if (thisv3 < thatv3) return -1;
						else if (thisv3 > thatv3) 	return 1;
						else return 0;}}
			}
		}

		static { // register this comparator
			WritableComparator.define(IntTriple.class, new Comparator());
		}
	}

	/**
	 * Compare only the first part of the pair, so that reduce is called once
	 * for each value of the first part.
	 */
	public static class FirstGroupingComparator implements RawComparator<IntTriple> {
		@Override
			public int compare(byte[] b1, int s1, int l1, byte[] b2, int s2, int l2) {
				return WritableComparator.compareBytes(b1, s1, Integer.SIZE/8*2, 
						b2, s2, Integer.SIZE/8*2);
			}
		@Override
			public int compare(IntTriple o1, IntTriple o2) {
				int l = o1.getV1(); int r = o2.getV1();
				int l2 = o2.getV1(); int r2 = o2.getV2();

				if  (l < r) return -1;
				else if (l > r) return 1;
				else {
					if (l2 < r2) return -1;
					else if (l2 > r2) return 1;
					else return 0;
				}
			}
	}



	/**
	 * Partition based on the first part of the pair.
	 */
	public static class FirstPartitioner extends Partitioner<IntTriple,IntWritable> {
		@Override
			public int getPartition(IntTriple key, IntWritable value, int numPartitions) {
				return Math.abs(key.getV1() * 127 + key.getV2()) % numPartitions;
			}
	}

	// Map
	public static class MMMapper extends Mapper<Object, Text, IntTriple, IntWritable>{
		private IntTriple keypair = new IntTriple();	
		private IntWritable valpair= new IntWritable();	
                private String Matrix1name;
                private String Matrix2name;
		private int n;	
		private int m;	
		protected void setup(Context context) throws IOException, InterruptedException {
                        Configuration config = context.getConfiguration();
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
		public void map(Object key, Text value, Context context
				) throws IOException, InterruptedException {
			StringTokenizer token = new StringTokenizer(value.toString());
			String mat = token.nextToken();
			int row = Integer.parseInt(token.nextToken());
			int col = Integer.parseInt(token.nextToken());
			int v = Integer.parseInt(token.nextToken());
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
	}

	// Reduce
        public static class MMReducer extends Reducer<IntTriple, IntWritable, Text, IntWritable> {
		private IntWritable val = new IntWritable();	
		private int l;	
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();

                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
		}
		public void reduce(IntTriple key, Iterable<IntWritable> values, Context context) 
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
                        System.err.println("Usage: <Matrix 1 name> <Matrix 2 name> <Number of row in Matrix 1><Number of columns in Matrix 1 (i.e., Number of rows in Matrix 2)> <Number of columns in Matrix 2> <in> <out>");
                        System.exit(2);
                }

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[6]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

                Job job = new Job(conf, "matrix multiplication 3: using secondary sort");
                Configuration config = job.getConfiguration();
                config.set("Matrix1name", otherArgs[0]);
                config.set("Matrix2name", otherArgs[1]);
                config.setInt("n",Integer.parseInt(otherArgs[2]));
                config.setInt("l",Integer.parseInt(otherArgs[3]));
                config.setInt("m",Integer.parseInt(otherArgs[4]));

                job.setJarByClass(MatrixMulti3.class);
                job.setMapperClass(MMMapper.class);
                job.setReducerClass(MMReducer.class);
                job.setMapOutputKeyClass(IntTriple.class);
                job.setMapOutputValueClass(IntWritable.class);
                job.setOutputKeyClass(Text.class);              // Output key type 선언
                job.setOutputValueClass(IntWritable.class);
                job.setNumReduceTasks(2);

                job.setPartitionerClass(FirstPartitioner.class);
                job.setGroupingComparatorClass(FirstGroupingComparator.class);

                FileInputFormat.addInputPath(job, new Path(otherArgs[5]));
                FileOutputFormat.setOutputPath(job, new Path(otherArgs[6]));
                System.exit(job.waitForCompletion(true) ? 0 : 1);
        }

}

