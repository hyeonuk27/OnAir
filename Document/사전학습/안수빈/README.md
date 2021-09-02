# 프로젝트 개요

> 병렬 분산 시스템과 맵리듀스 프레임워크를 이해하고 하둡을 이용하여 여러 빅데이터 분석 문제들에 대해서 맵리듀스 알고리즘을 자바 언어로 구현하고 실행한다.

- 병렬 분산 알고리즘 구현이 가능한 맵리듀스 프레임워크를 이해한다.
- 맵리듀스 프레임워크를 사용할 수 있는 하둡 설치 및 맵리듀스 알고리즘 코드를 실행한다.
- 하둡을 이용하여 빅데이터 분석 및 처리용 맵리듀스 알고리즘을 구현하는데 필요한 지식과 코딩 능력을 배양한다.

<br>

### 📃 학습내용

<details>
    <summary>1강</summary>
    <ul>
        <li><a href="1강/00_hadoop_env.md">Hadoop 설치</a></li>
        <li><a href="1강/01_hadoop.md">Hadoop</a></li>
        <li><a href="1강/02_map_reduce.md">MapReduce</a></li>
    </ul>
</details>
<details>
    <summary>2강</summary>
</details>

<br>

### 기본 코드 실행 명령어

```bash
# Project/src/Driver.java 파일 수정
pgd.addClass("wordcount", Wordcount.class);

$ cd /home/hadoop/Project
$ ant
$ hdfs dfs -rm -r wordcount_test_out

$ hadoop jar ssafy.jar wordcount wordcount_test wordcount_test_out
$ hdfs dfs -cat wordcount_test_out/part-r-00000|more
$ hdfs dfs -cat wordcount_test_out/part-r-00001|more
```

