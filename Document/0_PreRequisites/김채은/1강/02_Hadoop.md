# 03_Hadoop

>  Apache 프로젝트의 MapReduce Framework의 오픈소스

<br>

### 3-1. 하둡 분산 파일 시스템 HDFS

> Hadoop Distributed File System

- 빅데이터 파일을 여러 대의 컴퓨터에 나누어 저장
- 각 파일을 여러 개의 순차적인 블록으로 저장
- 하나의 파일의 블록은 폴트 톨러런스 Fault Tolerance를 위해 여러 개로 복사되어 여러 머신의 여기저기에 저장된다: 빅데이터를 수천대의 값 싼 컴퓨터에 병렬 처리하기 위해 분산한다

```bash
Fault Tolerance: 시스템을 구성하는 부품의 일부에서 결함 또는 고장이 발생하여도
                              정상적 / 부분적으로 기능을 수행할 수 있는 것
```

<br>

### 3-2. 구성 요소

- MapReduce: 소프트웨어의 수행을 분산한다
- Hadoop Distributed File System HDFS: 데이터를 분산한다
- 한 개의 Namenode (Master)와 여러 개의 Datanode(salves)
  - Namenode: 파일 시스템을 관리하고 클라이언트가 파일에 접근할 수 있도록 한다
  - Datanode: 컴퓨터에 들어있는 데이터를 접근할 수 있게 한다
