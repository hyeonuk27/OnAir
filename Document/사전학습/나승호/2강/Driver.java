package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
  public static void main(String[] args) {
    int exitCode = -1;
    ProgramDriver pgd = new ProgramDriver();
    try {

      pgd.addClass("wordcount1char", Wordcount1char.class, "A map/reduce program that counts the 1st.");
      pgd.addClass("wordcountsort", Wordcountsort.class, "A map/reduce program that output frequency of the words in the input files by alphabetical order.");
      pgd.addClass("invertedindex", InvertedIndex.class, "A map/reduce program that invert index");
      pgd.addClass("matrixadd", MatrixAdd.class, "A map/reduce program taht add matrix");
      pgd.driver(args);
      exitCode = 0;
    }
    catch(Throwable e) {
      e.printStackTrace();
    }

    System.exit(exitCode);
  }
}
