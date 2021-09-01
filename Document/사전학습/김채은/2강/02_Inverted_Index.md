# 02_Inverted Index

각각의 단어가 어느 문서의 어느 위치에 나타났는지를 리스트로 가지고 있는 것

<br>

## InvertedIndex.java 만들고 실행

| inverted_index                                               | concatenator_reducer                                         | main function                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![inverted_index](과제결과물/inverted_index//inverted_index.png) | ![concatenator_reducer](과제결과물/inverted_index/concatenator_reducer.png) | ![main function](과제결과물/inverted_index//main function.png) |

```bash

# Project/src/Driver.java 파일 수정
pgd.addClass("inverted", Wordcountsort.class, "A map/reduce program that generates the inverted index using words in the input files.");

cd /home/hadoop/Project
$ ant

# 이번에는 리듀스 함수의 결과를 출력하는 디렉토리를 맵리듀스 코드에서
# 자동적으로 삭제하도록 구현
$ hadoop jar ssafy.jar wordcount wordcount_test invertindex_test_out
$ hdfs dfs -cat invertindex_test_out/part-r-00000|more
$ hdfs dfs -cat invertindex_test_out/part-r-00001|more
```

