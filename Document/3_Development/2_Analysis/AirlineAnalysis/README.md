# [예측분석] Data Preprocessing

> 작성자 박지우
>
> 작성일자 2021.09.23



### Original Big Data

- `Data A`: 국토교통부 한국항공협회 Airportal 실시간운항정보 2017.01 ~ 2021.09

- `Data B`: OpenWeather 기상정보 2017.01 ~ 2021.09
- `Data C`: 인천국제공항공사 항공통계 항공사별 월 이용객 2017.01 ~ 2021.09



### 분석 목표

- 통계용 데이터

  | 목적                                                         | 전처리 목표                                                  |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | 지연사유별 건수 / 전체 지연 건수 (항공사별,  항공사별 목적지별) | A \|`Filter` Status == '지연'                                |
  | 취소사유별 건수 / 전체 취소 건수 (항공사별,  항공사별 목적지별) | A \| `Filter` Status == '취소'                               |
  | 월별 이용객                                                  | C \|  단순 시각화                                            |
  | 월별 평균 지연시간                                           | A \| DepartureTime - EstimateTime                            |
  | 지연사유별 평균 지연시간                                     | A \| `Filter` Status == '지연' Reason으로 sort하여 시각화    |
  | 기상환경별 평균 지연시간                                     | A + B \| `Filter` Status == '지연' Weather로 sort하여 시각화 |
  | 월 이용객별 평균 지연시간                                    | A + C \| `Filter` Status == '지연' 날짜 및 이용객수로 sort하여 시각화 |

  

- 머신러닝용 데이터

  | 목적                                                         | 전처리 목표                                               |
  | ------------------------------------------------------------ | --------------------------------------------------------- |
  | 기상환경에 따른 지연시간, 지연률 예측                        | A + B \| 로지스틱회귀 모델 및 선형회귀 모델 사용하여 학습 |
  | 월별 이용객(혼잡도)에 따른 지연시간, 지연률 예측             | A + C \|  ""                                              |
  | 기상환경 및 월별 이용객(혼잡도)에 따른 지연시간, 지연률 예측 | A + B + C \| ""                                           |

  

## Pandas 문법 정리

#### 기본 설정

- import

  ```python
  import pandas [as pd]
  ```

  

- csv 파일 불러오기 + 데이터 프레임에 할당

  ```python
  from pandas.io.parsers import read_csv
  
  df = read_csv('./filename.csv')
  ```

  

- csv 파일 내보내기

  ```python
  df.to_csv('./airlines.csv')
  ```



#### 행/열 추가, 수정, 삭제, 추출

#### - 추가

- 행 추가
- 열 추가

#### - 수정

- 행 수정
- 열 수정

#### - 삭제

- 행 삭제

- 열 삭제

  ```
  df.drop(colums=['column', 'column'], inplace=True)
  df = df.drop(colums=['column', 'column'])
  ```

  

#### - 중복

- 행 중복확인 및 삭제
- 열 중복확인 및 삭제

#### - 추출

- 특정 행 추출
- 특정 열 추출
- 특정 조건 추출



#### - Unnamed Column

```
input = pd.read_csv('data.csv', index_col = 0)
input.drop(['Unnamed: 0'], axis = 1, inplace = True)
```



#### 

#### 

- ```
  to_datetime()
  ```

- ```
  df = df.loc[df['airline'].isin(airline_set)]
  ```

- ```
   condition_type = df[df['type'] == '화물'].index
   df = df.drop(condition_type)
  ```

- ```
  df.loc[(df.togo == 'CEB()'), 'togo'] = 'CEB(세부)'
  ```

- ```
   df = df.drop(columns=['flightNo', 'type'])
  ```



https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=wideeyed&logNo=221578773214

