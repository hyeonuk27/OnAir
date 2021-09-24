package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
	public static void main(String[] args) {
		int exitCode = -1;
		ProgramDriver pgd = new ProgramDriver();
		try {

			pgd.addClass("wordcount", Wordcount.class, "A map/reduce program that performs word counting.");
			pgd.addClass("wordcount1char", Wordcount1char.class, "A map/reduce program that counts the 1st character of words in the input files.");
			pgd.addClass("wordcountsort", Wordcountsort.class, "A map/reduce program that output frequency of the words in the input files by alphabetical order.");
			pgd.addClass("inverted", InvertedIndex.class, "A map/reduce program that generates the inverted index using words in the input files.");
			pgd.addClass("matadd", MatrixAdd.class, "A map/reduce program that computes the addition of two matrices.");
			pgd.addClass("matmulti", 1-Phase MatrixMulti.class, "1-Phase Matrix Multiplication Preparation");
			pgd.addClass("allpair," AllPairPartition.class, "A map/reduce program that partitions all pairs of tuples from both tables.");
			pgd.addClass("allpairself," AllPairPartitionSelf.class, "A map/reduce program that partitions all pairs of tuples from a tables.");
      			pgd.driver(args);
			exitCode = 0;
		}
		catch(Throwable e) {
			e.printStackTrace();
		}

		System.exit(exitCode);
	}
}
