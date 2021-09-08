# [1강] MapReduce Intro & 기본 알고리즘(1)

## 목차

[요약](요약)

[설치과정](설치과정)

[과제](과제)

## 요약

- 병렬 분산 시스템이란?

  - Scale-out: 값싼 서버를 많이 배치함으로써 성능이 선형에 가깝게 증가하도록 함

  -> 이러한 값싼 서버(컴퓨터)를 묶어서 처리하는 것이 병렬 분산 시스템, 즉 MapReduce 프레임워크가 하는 일

- 맵리듀스 프레임워크란?

  - 병렬 분산 알고리즘 구현을 위한 프레임워크
  - 빅데이터를 이용한 효율적인 계산이 가능한 첫번째 프로그래밍 모델
  - 값싼 컴퓨터들을 모아서 클러스터를 만들고 빅데이터를 처리하기 위한 scalable(사용자 또는 데이터가 급증하여도 프로그램이 멈추거나 성능이 크게 떨어지지 않는) 병렬 소프트웨어의 구현을 쉽게 할 수 있도록 도와주는 간단한 프로그래밍 모델

- Hadoop이란?

  - 구글이 개발한 Apache Project의 맵리듀스 프레임워크 오픈소스
  - 드라이버(`Driver.java`)에 해당하는 메인 함수가 맵(`map`) 함수와 리듀스(`reduce`) 함수를 호출해 처리한다. (소프트웨어 수행 분산)
  - 하둡 분산 파일 시스템 (Hadoop Distributed File System - HDFS) (데이터 분산)
    - 각 파일을 여러 개의 순차적인 블록으로 저장함
    - 하나의 파일의 각 블록은 여러 머신 여기 저기에 저장된다. (fault tolerance)
  - Namenode(master) & Datanode(slaves)

- 맵리듀스 프로그래밍 언어의 형태

  - Main 함수
    - master machine에서 수행
    - map 함수 수행 전에 전처리를 하거나 리듀스 함수의 결과를 후처리 하는데 사용할 수 있다.
  - MapReduce Phase 
    - Map Phase
      - Map 함수: key, value의 형태, 라인 단위로 호출
      - 데이터의 여러 파티션에 병렬 분산으로 호출되어 수행된다.
    - Combine 함수: Reduce 함수와 유사, Map 함수의 출력 크기를 줄여서 Shuffling, Reduce 페이즈의 비용을 줄여준다. (수행하지 않을 수 있다.)
    - Shuffling Phase
      - Map Phase가 다 끝나면 시작된다.
      - Key로 Sorting -> Value-list 만들어 분산하여 보낸다.
    - Reduce Phase
      - Shuffling Phase가 다 끝나면 시작된다.
      - 각 (key, value-list) 쌍 마다 함수 호출
      - Reduce 함수: key, value의 형태 (수행하지 않을 수 있다.)



## 설치과정



## 과제



