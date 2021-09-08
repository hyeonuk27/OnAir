# 01_Matrix Multiplication

- 

<br>

## Wordcountsort.java 만들고 실행

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |

```bash
# Project/src/Driver.java 파일 수정
pgd.addClass("wordcountsort", Wordcountsort.class, "A map/reduce program that output frequency of the words in the input files by alphabetical order.");

$ cd /home/hadoop/Project
$ ant
$ hdfs dfs -rm -r wordcount1char_test_out

$ hadoop jar ssafy.jar wordcount wordcount_test wordcountsort_test_out
$ hdfs dfs -cat wordcountsort_test_out/part-r-00000|more
$ hdfs dfs -cat wordcountsort_test_out/part-r-00001|more
```

