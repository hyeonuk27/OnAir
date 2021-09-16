import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;


public class TwoWayJoinGenerator {
	/*
	public static final int JOIN_PREDICATE_EQUAL = 0;
	public static final int JOIN_PREDICATE_LTE = -1;
	public static final int JOIN_PREDICATE_LT = -2;
	public static final int JOIN_PREDICATE_RTE = 1;
	public static final int JOIN_PREDICATE_RT = 2;*/
	
	int nR 		= 10;		//Number of tuples in R;
	int nS		= 10;		//Number of tuples in S;
	int range	= 5;		//range of values [0, range)
	int nAttrs	= 3;		//Number of attributes;
	int seed	= 0;		//seed
	//int joinattr= 1;		//Join attribute
	//int join_predicate = JOIN_PREDICATE_EQUAL;
	
	public static void main(String[] args) throws IOException{		
		//Parameter Settings;
		if(args.length!=5){
			System.out.printf("usage: <seed> <number of records in R> <number of records in S> <max value of attributes> <number of attributes in both tables>");  
			System.exit(0);
		}
		int seed = Integer.parseInt(args[0]);
		int nR = Integer.parseInt(args[1]);
		int nS = Integer.parseInt(args[2]);
		int range = Integer.parseInt(args[3]);
		int nAttrs = Integer.parseInt(args[4]);
		
		TwoWayJoinGenerator dg = new TwoWayJoinGenerator(nR, nS, range, nAttrs, seed);
		dg.generate();
		
	}
	public TwoWayJoinGenerator(int nR, int nS, int range, int nAttrs, int seed){
		this.nR = nR;
		this.nS = nS;
		this.range = range;
		this.nAttrs = nAttrs;
		this.seed = seed;
	}
	public void generate() throws IOException{
		Random r = new Random(seed);
		
		ArrayList<Record> records_R = new ArrayList<Record>();
		for(int id = 1; id<=nR; id++){
			Record nr = new Record("R",id, r, nAttrs, range);
			records_R.add(nr);
		}
		
		ArrayList<Record> records_S = new ArrayList<Record>();
		for(int id = 1; id<=nS; id++){
			Record ns = new Record("S",id, r, nAttrs, range);
			records_S.add(ns);
		}
		ArrayList<Record> records = new ArrayList<Record>();
		records.addAll(records_R);
		records.addAll(records_S);
		String filename = "twowayjoin-"+nR+"-"+nS+"-"+range+"-"+nAttrs+"-data.txt";
		writeArrayList(filename, records);
	}
	
	public static <T> void writeArrayList(String filename, ArrayList<T> list) throws IOException{
		BufferedWriter bw = new BufferedWriter(new FileWriter(filename));
		
		for(int i = 0; i <list.size(); i++){
			bw.write(list.get(i).toString());
			bw.newLine();
		}
		
		bw.close();
		System.out.println(filename+" is generated!");
	}
	
	
	
}

/*
class RecordPair{
	Record r;
	Record s;
	public RecordPair(Record r, Record s){
		this.r = r;
		this.s = s;
	}
	public String toString(){
		return r.toString()+"\t"+s.toString();
	}
}
*/
class Record{
	String tablename;
	int[] vals;
	public Record(String tablename, int id, Random r, int nAttrs, int range){
		this.tablename = tablename;
		vals = new int[nAttrs];
		vals[0] = id;
		for(int c = 1; c<nAttrs; c++){
			vals[c] = r.nextInt(range);
		}
	}
	
	public String toString(){
		String out = "";
		out += tablename+"\t";
		for(int c = 0; c<vals.length; c++){
			out+=vals[c];
			if(c!=vals.length-1){
				out+="\t";
			}
		}
		
		return out;
	}
}
