package ssafy;

import java.io.IOException;
import java.util.Random;
import java.lang.Math;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class KMeans {

	public static class MapperClass
			extends Mapper<Object,Text,IntWritable,Text> {

		private int dimension = 2;
		private IntWritable emitKey = new IntWritable();
		private Text emitval = new Text();

		// IMPORTANT: the number of clusters
		private int K;
		// IMPORTANT: the vectors for cluster centers
		private double[][] centers =  null;
		private double[] point = null;
			
		// get the parameters set by the main function (see the main function. we call "conf.set")
		//
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
			// get the parameter of name "k"
			// 2 is the default value (getInt returns the default value if the param of "k" is not set)
			K = config.getInt ("K", 2);
			dimension = config.getInt ("dimension", 2);
			// we have k number of cluster centers
			centers = new double[K][dimension];
			// get the vectors of the k cluster centers 
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------

		}

		// map function (Object, Text : input key-value pair
		//               Context : fixed parameter)
		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {
				
			int which_center = 0;
			stringToDoubleArray (value.toString(), dimension, point);

			// get the vectors of the k cluster centers 
			// emit a key-value pair 
			//   emitKey : cluster id that the input point belongs to
			//   value : the input point and the squared error of the current point 
			//           with the coses center
			//context.write (emitKey, valudde);
                        // TODO
                        // ------------------------------------------------------
                        //
                        // ------------------------------------------------------
			emitKey.set (which_center);
			context.write (emitKey, emitval);
		}
	}
	

	/*
	 * ReducerClass
	 */
	public static class ReducerClass
			extends Reducer<IntWritable,Text,IntWritable,Text> {

		private Text result = new Text();
		private int dimension = 2;

		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();

			// get the parameter of name "k"
			// 2 is the default value (getInt returns the default value if the param of "k" is not set)
			dimension = config.getInt ("dimension", 2);

		}

		public void reduce(IntWritable key, Iterable<Text> values, Context context) 
				throws IOException, InterruptedException {
			double[] sum = new double [dimension+1];
			double[] point = new double [dimension+1];
			int count = 0;
                        // TODO
                        // ------------------------------------------------------
                        //
			// -------------------------------
		}
	}


	/*
	 * return the square of the Euclidean distance between two points
	 * ( we do not compute the square root )
	 */
	public static double computeDistance (double[] arr1, double[] arr2, int d) {
		if (arr1.length < d || arr2.length < d)
			return -1;

		double sum = 0;
		for (int i=0; i<d; i++) {
			sum += (arr1[i] - arr2[i]) * (arr1[i] - arr2[i]);
		}
		return sum;
	}


	/*
	 * convert a double type array to a string
	 */
	public static String doubleArrayToString (double[] arr, int d) {
		String str = "";
		if (d == 0) return str;

		str += arr[0];
		for (int i=1; i<d; i++) {
			str += "\t" + arr[i];
		}
		return str;
	}

	/*
	 * convert a string to a double type array
	 */
	public static boolean stringToDoubleArray (String str, int d, double[] arr) {
		if (arr.length < d)
			return false;

		String[] strarr = str.split ("\t");
		for (int i=0; i<strarr.length && i<d; i++) {
			arr[i] = Double.parseDouble (strarr[i]);
		}
		return true;
	}

	// Given center ID, return the output filename
	public static String getFilename (int cid) {
               	int count = 0;
		int num = cid;
		String filename="/part-r-";
		if (num == 0)
			filename="/part-r-00000";
		else {
                         // TODO
                         // ------------------------------------------------------
                         //
                         // ------------------------------------------------------
		}
		return filename;
	}

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf,args).getRemainingArgs();
		if ( otherArgs.length != 7 ) {
			System.err.println("Usage: <seed> <dimension> <K> <maxIter> <epsilon> <in> <out>");
			System.exit(2);
		}


                long seed = Long.parseLong(otherArgs[0]);
                int dimension = Integer.parseInt(otherArgs[1]);
                int K = Integer.parseInt(otherArgs[2]);
                int maxIter = Integer.parseInt(otherArgs[3]);
                double epsilon  = (double) Float.parseFloat(otherArgs[4]);
                if (maxIter <5) {
                        System.err.println("<MaxIter> should be at least 5!");
                        System.exit(2);
                }
                double[] center = new double [dimension];
		// initial centers
		Random rand = new Random(seed);
		// broadcasted to the map functions by using "conf.set"
		conf.setInt("dimension", dimension);
		conf.setInt("K", K);
		for(int cid = 0 ; cid < K ; ++cid) {
			String name = "strCenters." + cid;
			String value = "" + (rand.nextFloat()*10);
			for(int dim = 1 ; dim < dimension ; ++dim)
				value += "\t" + (rand.nextFloat()*10);
			conf.set(name, value);
		}
		

		double prevSSD = 10000000, newSSD = 0;
		int itr=0;
		int iterationFlag = 1;
                while ((iterationFlag == 1) && (itr<maxIter) )  {
			Job job = new Job(conf,"k-means clustering");
			job.setJarByClass(KMeans.class);

			// let hadoop know the map and reduce classes
			job.setMapperClass(MapperClass.class);
			job.setReducerClass(ReducerClass.class);

			// let hadoop know the key-value pair type
			job.setOutputKeyClass(IntWritable.class);
			job.setOutputValueClass(Text.class);

			// set number of reduce functions (let's use 1 in the example, do not change!!)
			job.setNumReduceTasks(K);

			String outputdirectory = otherArgs[6] + itr;
                        int tmpnum = itr - 2;
			String deletedirectory = otherArgs[6] + tmpnum;
                        if (itr >=2) { 
			        Path deletedir = new Path (deletedirectory);
				if (FileSystem.get(conf).exists(deletedir)) {
					FileSystem.get(conf).delete (deletedir);
				}	
                        }

                        Path outdir = new Path (outputdirectory);
                        if (FileSystem.get(conf).exists(outdir)) {
                                FileSystem.get(conf).delete (outdir);
                        }


			// read the output of reduce function to obtain the updated cluster centers
			// the updated cluster centers are broadcasted again
			FileInputFormat.addInputPath(job,new Path(otherArgs[5]));
			FileOutputFormat.setOutputPath(job,new Path(outputdirectory));
			job.waitForCompletion(true);

			newSSD = 0;
			FileSystem fs = outdir.getFileSystem (conf);
			for (int cid = 0; cid < K; cid++) {

				//FSDataInputStream fp = fs.open (new Path (outdir + "/part-r-0000"+cid));
				FSDataInputStream fp = fs.open (new Path (outdir + getFilename(cid)));
 
				String line = null;
				while ( (line = fp.readLine ()) != null ) {
					String[] arr = line.split("\t");
					int centerId = Integer.parseInt (arr[0]);
					for (int i=1; i<=dimension; i++)
						center[i-1] = Double.parseDouble (arr[i]);
					conf.set ("strCenters." + centerId, doubleArrayToString (center, dimension));
					newSSD = Math.sqrt(Double.parseDouble (arr[dimension+1]));
				}
			}

                        if ((itr >= 5) && (Math.abs(prevSSD - newSSD)/Math.abs(newSSD)) <= epsilon) {
                                iterationFlag = 0;
                                System.out.println("ErrorRatio: " + (Math.abs(prevSSD - newSSD)/Math.abs(newSSD)));
                        }
                        prevSSD = newSSD;
                        itr++;
		}
                System.out.println("Number of Iterations: "+(itr-1));
                String resultdir = otherArgs[6] + (itr - 2);
                System.out.println("Please look at the HDFS directory " + resultdir +" for clustering result!");
	}
}
