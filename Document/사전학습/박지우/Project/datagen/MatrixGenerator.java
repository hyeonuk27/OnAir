import java.io.File;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.TreeSet;
import java.io.FileOutputStream;

public class MatrixGenerator {

	public MatrixGenerator() {
		// TODO Auto-generated constructor stub
	}
	
	public static void main( String[] argv ) {
		if ( argv.length != 8 ) {
                        System.err.println("Usage: <seed> <Matrix 1 name> <Matrix 2 name> <Number of row in Matrix 1><Number of columns in Matrix 1 (i.e., Number of rows in Matrix 2)> <Number of columns in Matrix 2> <datafilename> <resultfilename>");


			System.exit(1);
		}		


		long seed = Long.parseLong( argv[0] );
                String Matrix1name = argv[1]; 
                String Matrix2name = argv[2];
		int n = Integer.parseInt( argv[3] );
		int l = Integer.parseInt( argv[4] );
		int m = Integer.parseInt( argv[5] );
                String datafilename = argv[6]; 
                String resultfilename = argv[7];

		int M1[][] = new int[n][l];
		int M2[][] = new int[l][n];

		Random rand = new Random(seed);

                try {
                        BufferedWriter bw1 = new BufferedWriter( new FileWriter( datafilename ) );

			for (int i = 0; i< n; i++){
				for (int j = 0; j< l; j++){
					int element = (int )(rand.nextGaussian()*10); 
					M1[i][j] = element;
					String line = Matrix1name + "\t" + i + "\t" + j + "\t" + element + "\n";
                                	bw1.write(line);
				}
			}	
			for (int i = 0; i< l; i++){
				for (int j = 0; j< m; j++){
					int element = (int )(rand.nextGaussian()*10); 
					M2[i][j] = element;
					String line = Matrix2name + "\t" + i + "\t" + j + "\t" + element + "\n";
                                	bw1.write(line);
				}
			}	
                        bw1.flush(); bw1.close();
                } catch ( IOException e ) { e.printStackTrace(); }


                try {
                        BufferedWriter bw2 = new BufferedWriter( new FileWriter( resultfilename ) );

			for (int i = 0; i< n; i++){
				for (int j = 0; j< m; j++){
					int sum = 0;
                                	for (int k = 0; k < l; k++)
						sum = sum + M1[i][k]*M2[k][j];
					String line = "" + i + " " + j + "\t" + sum + "\n";
                                	bw2.write(line);
						//System.out.println(""+i+k+j);
				}
			}
                        bw2.flush(); bw2.close();
                } catch ( IOException e ) { e.printStackTrace(); }
	}
}
