import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Random;

public class KMeansGenerator {
	public static void main( String args[] ) throws Exception {
		if( args.length != 4 ) {
			System.out.println( " <seed> <dimension> <number of clusters> <number of points>" );
			System.exit( 0 );
		}
		int seed = Integer.parseInt( args[ 0 ] );
		int dimension = Integer.parseInt( args[ 1 ] );
		int nCluster = Integer.parseInt( args[ 2 ] );
		int nPoint = Integer.parseInt( args[ 3 ] );

		BufferedWriter bw = new BufferedWriter( new FileWriter( "kmeans-" + seed + "-" + dimension + "-" + nCluster + "-" + nPoint + "-data.txt" ) );

		Random rn = new Random( seed );

		double[][] center = new double[ nCluster ][ dimension ];
		for( int i = 0; i < nCluster; i++ ) {
			for( int j = 0; j < dimension; j++ ) {
				center[ i ][ j ] = rn.nextInt( 10 );
			}
		}

		for( int i = 0; i < nPoint; i++ ) {
			int first = 1;
			for( int d = 0; d < dimension; d++ ) {
				if (first == 1) {
					first = 0;
					bw.write( Double.toString( center[ ( i % nCluster ) ][ d ] + rn.nextGaussian() ) );
				}
				else {
					first = 0;
					bw.write( "\t" );
					bw.write( Double.toString( center[ ( i % nCluster ) ][ d ] + rn.nextGaussian() ) );
				}
			}
			bw.write( "\n" );
		}

		bw.close();
	}
}
