# 03_Matrix Addition

<br>

## MatrixAdd.java 만들고 실행

| matrixAdd                                              | main function                                                | driver                                           |
| ------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------ |
| ![matrixAdd](과제결과물/matrix_addition/matrixAdd.PNG) | ![main_function](과제결과물/matrix_addition/main_function.PNG) | ![driver](과제결과물/matrix_addition/driver.PNG) |

```bash
# Project/src/Driver.java 파일 수정
pgd.addClass("matadd", MatrixAdd.class, "A map/reduce program computes the addition of two matrices.");

$ cd /home/hadoop/Project
$ ant
$ hdfs dfs -put data/matadd-data-2x2.txt matadd_test
$ hadoop jar ssafy.jar matadd matadd_test matadd_test_out

$ hdfs dfs -cat matadd_test_out/part-r-00000|more
$ hdfs dfs -cat matadd_test_out/part-r-00001|more
```

