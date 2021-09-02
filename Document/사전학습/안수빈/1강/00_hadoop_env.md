[TOC]

# Hadoop 설치

## 1. 개발 환경 구성

### 1) VMware 설치

> 윈도우에서 리눅스 OS를 실행할 수 있도록 하는 역할을 한다.

- 홈페이지 하단 DOWNLOAD 버튼을 통해서 최신버전 설치
  - [VMware download](https://www.vmware.com/products/workstation-player.html)

### 2) Ubuntu 설치

> 가장 많이 사용하는 리눅스 OS이다.

- CD image (iso file) 다운로드
  - [Ubuntu download](https://ubuntu.com/download/desktop)
- VMware 실행 후, `Create a New VM` 선택
- 다운받은 Ubuntu image를 올려서 새로운 가상머신을 생성
- hadoop 계정 생성
  - Full name : ubuntu
  - User name : hadoop

### 3) Hadoop 설치 : Standalone 모드

1. 패키징된 파일 다운로드

```bash
# /~ 에서 실행
$ wget <http://kdd.snu.ac.kr/~kddlab/Project.tar.gz>
```

2. hadoop 설치

```bash
$ tar zxf Project.tar.gz

$ sudo chown -R hadoop:hadoop Project

$ cd Project

$ sudo mv hadoop-3.2.2 /usr/local/hadoop

$ sudo apt update

$ sudo apt install ssh openjdk-8-jdk ant -y

$ ./set_hadoop_env.sh

# path를 지정
$ source ~/.bashrc
```

<br>

## 2. Hadoop 실행을 위한 준비

> `/~` 에서 실행

1. Empty `ssh key` generation
   - password 입력없이 실행시키도록 하기 위한 작업

```bash
# 저장할 파일 물어보면 enter만 실행
$ ssh-keygen -t rsa -P ""

$ cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys

# 제대로 생성되었는지 확인
$ ssh localhost
# 질문이 뜨면 yes -- 비밀번호 묻지 않고 진행되면 성공
```

2. 모든 명령은 hadoop 계정에서 실행

```bash
# Name Node format
# 하둡 파일 시스템 포맷
$ hadoop namenode -format

# Dfs daemon start
# 분산 파일 시스템 데몬 띄우기
$ start-dfs.sh

# MapReduce daemon start (standalone 모드에서는 불필요)
# 맵리듀스 데몬 띄우기
# $ start-mapred.sh

# 수행 중인 java 프로세스 리스트 확인 
# NameNode, SecondaryNameNode, DataNode, (TaskTracker, JobTracker)
$ jps
```

3. hadoop 디렉토리

```bash
# hadoop 계정의 HDFS 디렉토리 확인
$ hdfs dfs -ls /

# hadoop 계정의 HDFS의 상위에 user 디렉토리 생성
$ hdfs dfs -mkdir /user

# hadoop 계정의 HDFS 상에서 /user 디렉토리 안에 hadoop 디렉토리 생성
$ hdfs dfs -mkdir /user/hadoop
```

<br>

## 3. Linux와 HDFS

> 데이터 생성이나 코딩은 Linux에서 하고, MapReduce 코드와 입력 데이터는 HDFS에 옮겨서 MapReduce 알고리즘을 수행한다.

- Linux 디렉토리
  - src/ (맵리듀스코드: 실제 코드를 넣는 디렉토리)
    - Driver.java (맵리듀스 코드 컴파일을 위한 파일)
    - Wordcount.java
  - template/ (과제를 위한 template) 
  - datagen/ (과제 데이터를 생성하기 위한 코드) 
  - data/ (과제를 위한 데이터) 
  - build.xml (맵리듀스 코드 컴파일을 위한 파일)

- Hadoop 디렉토리
  - wordcount_test/ (맵리듀스 코드 실행을 위한 데이터 디렉토리) 
  - wordcount_test_out/ (맵리듀스 코드 실행 결과를 저장하는 디렉토리)

