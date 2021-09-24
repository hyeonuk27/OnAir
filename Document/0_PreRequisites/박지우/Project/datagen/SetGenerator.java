import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.TreeSet;

public class SetGenerator {

	public SetGenerator() {
		// TODO Auto-generated constructor stub
	}
	
	public static void main( String[] argv ) {

                if ( argv.length != 4 ) {
				System.err.println( "usage: <seed> <number of records> <number of items(max: 26)> <datafilename>" );
                        System.exit(1);
                }

		long seed = Long.parseLong( argv[0] );
		int n = Integer.parseInt( argv[1] );
		int m = Math.min( Integer.parseInt( argv[2] ), 26);
		Random rand = new Random(seed);
		int len_avg = (int)Math.round( Math.sqrt(m) )+1;
		double std = (m - len_avg) / 3;
		int len;
		TreeSet<Integer> set = new TreeSet<Integer>();
		
		try {
			BufferedWriter bw = new BufferedWriter( new FileWriter( argv[3] ) );
			for ( int i=0; i<n; i++ ) {
				len = Math.max(1, (int)( rand.nextGaussian()*std + len_avg ) );
				len = Math.min( len, m );
				set.clear();
				while ( set.size() < len ) {
					set.add( (int)(rand.nextDouble()*m)+65 );
				}
				StringBuilder strbld = new StringBuilder();
				strbld.append(i+"\t");
				for ( int item : set ) {
					strbld.append((char)item+" " );
				}
				bw.write(strbld.toString().trim()+'\n');
			}
			bw.flush(); bw.close();
		} catch ( IOException e ) { e.printStackTrace(); }
		System.out.println( "Data "+argv[3]+" is successfully generated." );
	}

	private static void usage() {
		System.err.println( "usage: seed output_path number_of_records number_of_items(max: 26)" );
	}
}
