import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.TreeSet;

public class VecSimJoinGenerator {

	public VecSimJoinGenerator() {
		// TODO Auto-generated constructor stub
	}
	
	public static void main( String[] argv ) {
		if ( argv.length != 4 ) {
			System.err.println( "usage:  <seed> <number of records> <dimension> <datafilename>" );
			System.exit(1);
		}		
		long seed = Long.parseLong( argv[0] );
		int numS = Integer.parseInt( argv[1] );
		int dimS = Integer.parseInt( argv[2] );
	        String datafilename = argv[3];

		Random rand = new Random(seed);


                try {
                        BufferedWriter bw1 = new BufferedWriter( new FileWriter( datafilename ) );

			for (int i = 0; i< numS; i++){
				String line = "" + i;
				for (int j = 0; j< dimS; j++)
					line = line + "\t" + (int )(rand.nextGaussian()*10);
				line = line + "\n";
                                bw1.write(line);
			}
                        bw1.flush(); bw1.close();
                } catch ( IOException e ) { e.printStackTrace(); }

	}

}
