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

public class MatrixMulti {
  // Map
  public static class MMMapper extends Mapper<Object, Text, Text, Text>{
    private Text keypair = new Text();      //
    private Text valpair= new Text();       //
    private String Matrix1name;
    private String Matrix2name;
    private int n;  // number of rows in matrix 1
    private int m;  // number of columns in matrix 2
    private int l;  // number of columns in matrix 1
    protected void setup(Context context) throws IOException, InterruptedException {
      Configuration config = context.getConfiguration();
      Matrix1name = config.get("Matrix1name", "A");
      Matrix2name = config.get("Matrix2name", "B");

      n = config.getInt("n", 10);
      m = config.getInt("m", 10);
      l = config.getInt("l", 10);
    }
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
      StringTokenizer token = new StringTokenizer(value.toString());
      String mat = token.nextToken();
      int row = Integer.parseInt(token.nextToken());
      int col = Integer.parseInt(token.nextToken());
      int v = Integer.parseInt(token.nextToken());

      if (mat.equals(Matrix1name)) {
        valpair.set(""+col+" "+v);
        for (int j = 0; j < m; j++) {
          String p = ""+row+","+j;
          keypair.set(p);
          context.write(keypair, valpair);
        }
      }
      else if (mat.equals(Matrix2name)) {
        valpair.set(""+row+" "+v);
        for (int j = 0; j < n; j++) {
          String p = ""+j+","+col;
          keypair.set(p);
          context.write(keypair, valpair);
        }
      }
    }
  }
  // Reduce
  public static class MMReducer extends Reducer<Text, Text, Text, Text> {
    private IntWritable val = new IntWritable();
    private int l;

    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
      for (Text tx: values) {
        context.write(key, tx);
      }
    }
  }
  // Main
  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    if (otherArgs.length != 7) {
      System.err.println("Usage: <Matrix1name> <Matrix2name>  <n> <m> <l> <in> <out>");
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

    job.setJarByClass(MatrixMulti.class);
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


