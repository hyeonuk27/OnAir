# 02_MapReduce Framework

[TOC]

값 싼 컴퓨터들을 모아서 클러스터를 만들고 여기에서 빅데이터를 처리하기 위한 스케일러블 병렬 소프트웨어의 구현을 쉽게 할 수 있도록 도와주는 간단한 프로그래밍 모델

**데이터 중심 프로세싱 (Data Intensive Processing)**

- 한 대의 컴퓨터의 능력으로 처리가 어려우므로 수십대, 수백대 혹은 수천대 컴퓨터를 묶어서 처리해야하는 역할

- 빅데이터를 이용한 효율적인 계산이 가능한 첫 번째 프로그래밍 모델: 기존에 존재하는 여러 가지 다른 병렬 컴퓨팅 방법에서는 프로그래머가 낮은 레벨의 시스템 세부 내용까지 아주 잘 알고 많은 시간을 쏟아야했다

```bash
scalable 하다: 사용자 수가 급증하거나 데이터가 급증해도 프로그램이 멈추거나 
							 성능이 크게 떨어지는 일이 없다
```

- MapReduce Framework의 구현: 구글의 MapReduce, Hadoop
- 드라이버에 해당하는 Main 함수가 Map 함수와 Reduce 함수를 호출해서 처리한다

<br>

---

<br>

## 1. MapReduce Programming Model

- 함수형 프로그래밍 언어의 형태
- 유저는 아래의 3가지 함수를 구현해서 제공
  - Main 함수
  - Map 함수: `(key1, val1) → [(key2, val2)]`
  - Reduce 함수: `(key2, [val2]) → [(key3, val3)]`
- 각각의 레코드 record 또는 튜플 tuple이 key-value 쌍으로 표현된다
- 마스터 머신 Master Machine
  - Main 함수를 한 개의 마스터 머신에서 수행
  - Map 함수를 수행하기 전에 전처리하거나 Reduce 함수의 결과를 후처리

<br>

---

<br>

## 2. MapReduce Phase

- Map과 Reduce 라는 유저가 정의한 함수 한 쌍으로 이루어진다
- 컴퓨팅에 의해 한 번 혹은 여러 번 반복 수행 가능
- Map함수 호출 - (Combine 함수 호출) - Reduce 함수 호출
- 드라이버에 해당하는 메인 프로그램에서 수행

**1단계: 맵 페이즈 Map Phase**

```
- 데이터의 여러 파티션에 병렬 분산으로 호출되어 수행
- 각 머신마다 Mapper가 입력 데이터의 한 줄마다 맵 함수를 호출한다
- Map함수는 (key, value)쌍 형태로 결과 출력하고 같은 key를 가진 (key, value) 쌍은 같은 머신으로 보낸다
```

**2단계: 셔플링 페이즈 Shuffling Phase**

```
- 모든 머신에서 맵 페이즈가 다 끝나면 시작
- 맵 페이즈에서 해당 머신으로 보내진 (key, value) 쌍을 key를 이용해 정렬한 후 (key, value-list) 형태로 같은 key에 따라 여러 머신에 분산해서 보낸다
```

**3단계: 리듀스 페이즈 Reduce Phase**

```
- 모든 머신에서 셔플링 페이즈가 다 끝나면 시작
- 셔플링 페이즈에서 해당 머신으로 보내진 (key, value-list) 쌍마다 순차적으로 리듀스 함수가 호출
- 출력이 있다면 (key, value) 쌍 형태로 호출
```
