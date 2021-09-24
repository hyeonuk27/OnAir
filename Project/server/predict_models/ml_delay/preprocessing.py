import pandas as pd
import glob

# 전처리 필요사항
# 통계용 - 날짜, 항공사, 목적지, 월별 이용객수, 상태, 지연시간(분), 지연사유
# 머신러닝용 - 항공사, 목적지, 월별 이용객수, 날씨, 지연여부(0, 1)(로지스틱회귀용), 지연시간(분)(다중선형회귀용)

# 통계 전처리
# 0. date, airport, togo, type, state열이 빈문자열이면 삭제
# 1. 항공사 우리 것으로 필터링
# 2. type가 화물인 행 제거
# 3. CEB()는 CEB(세부)로 바꾸기
# 4. flightNo, type 열 삭제
# 5. date열 날짜 타입으로 바꾸고 년, 월, 일 뽑아와서 년, 월로 월별 이용객수 열 추가 -> merge 이용
# 6. delayedTime 열 추가, state가 지연일 경우에만 departTime - originTime, 나머지는 0 -> 한 다음 originTime, departTime 열 삭제

# 머신러닝 전처리
# 1 ~ 6 동일
# 7. state열이 취소면 삭제
# 8. 년, 월, 일로 날씨 추가
# 9. isDelayed 열 추가, 지연일 경우에 1, 출발/취소일 경우에 0

# 공통
# 10. 추가 - 운행기록이 통계 데이터 기준 500번 이하인 나라는 제거 (머신러닝은 그에 맞춤)

# 목적지 모으기(DB용)
# 목적지 열 csv뽑기

airline_set = {
    '중국남방항공', 
    '중국동방항공', 
    '델타항공', 
    '네덜란드항공', 
    '대한항공', 
    '카타르항공', 
    '아메리칸항공', 
    '아시아나항공', 
    '독일항공', 
    '에미레이트항공', 
    '캐나다항공', 
    '유나이티드항공', 
    '프랑스항공',
    '진에어',
    '티웨이항공',
    '제주항공',
    '에어서울'
}

# 월별 이용객수 데이터 전부 합치기
df_passengers = pd.DataFrame()
airline_list = [
    '네덜란드항공', '대한항공', '델타항공', '독일항공', '아메리칸항공', '아시아나항공', '에미레이트항공', '프랑스항공', '에어서울', 
    '유나이티드항공', '제주항공', '중국남방항공', '중국동방항공', '진에어', '카타르항공', '캐나다항공', '티웨이항공']

for idx, f in enumerate(glob.glob('./passengers/*.csv')):
    df = pd.read_csv(f)
    df.insert(2, 'airline', [airline_list[idx]] * df.shape[0])
    df_passengers = pd.concat([df_passengers, df])

df_passengers.drop(['Unnamed: 0'], axis = 1, inplace = True)
df_passengers['date'] = pd.to_datetime(df_passengers['date'], format='%Y-%m-%d')
df_passengers['year'] = pd.DatetimeIndex(df_passengers['date']).year
df_passengers['month'] = pd.DatetimeIndex(df_passengers['date']).month

# 항공 데이터 전처리
df_statistics = pd.DataFrame()
df_ml = pd.DataFrame()

for f in glob.glob('./data/*.csv'):
    df = pd.read_csv(f)
    # 0.
    df.dropna(subset=['date', 'airline', 'togo', 'type', 'state'], inplace=True)

    # 1.
    df = df.loc[df['airline'].isin(airline_set)]

    # 2.
    condition_type = df[df['type'] == '화물'].index
    df = df.drop(condition_type)

    # 3.
    df.loc[(df.togo == 'CEB()'), 'togo'] = 'CEB(세부)'

    # 4.
    df = df.drop(columns=['flightNo', 'type'])
    
    # 5.
    # https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221535156243
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month
    df = pd.merge(left=df, right=df_passengers, how='left', on=['year', 'month', 'airline'], sort=False)
    df.dropna(subset=['passengers'], inplace=True)
    df['passengers'] = df['passengers'].astype(int)

    # 6.
    df_delayed = df[df['state'] == '지연']
    df_not_delayed = df[df['state'] != '지연']
    # 지연인데도 출발 시각이 안찍힌 아이들
    df_delayed = df_delayed[df_delayed['departTime'] != ':']
    # 날짜와 시간을 합치는 방법(중요)
    temp_dt = df_delayed['departTime'] # 머신러닝에서 df_not_delayed 부분까지 일괄적으로 날짜 형식을 바꿔주기 위해 저장해둠
    df_delayed['departTime'] = pd.to_timedelta(df_delayed['departTime'] + ':00') + df_delayed['date_x']
    df_delayed['originTime'] = pd.to_timedelta(df_delayed['originTime'] + ':00') + df_delayed['date_x']
    df_delayed['delayedTime'] = df_delayed['departTime'] - df_delayed['originTime']
    df_delayed['delayedTime'] = df_delayed['delayedTime'].astype('timedelta64[m]').astype(int)
    df_not_delayed['delayedTime'] = [0] * df_not_delayed.shape[0]
    df = pd.concat([df_delayed, df_not_delayed])
    df.rename(columns = {'date_x' : 'date'}, inplace = True)
    df = df.drop(['originTime', 'departTime', 'date_y', 'year', 'month'], axis=1)
    # 머신러닝에서 쓰기 위해 복원
    df_delayed['departTime'] = temp_dt
    df2 = pd.concat([df_delayed, df_not_delayed])
    df2.rename(columns = {'date_x' : 'date'}, inplace = True)
    df2 = df2.drop(['originTime', 'date_y', 'year', 'month'], axis=1)

    # 머신러닝
    # 7. 
    condition_state = df2[df2['state'] == '취소'].index
    df2 = df2.drop(condition_state)

    # 8.
    # weather.csv를 weather_preprocessing.py를 통해 전처리한 상태의 Dataframe을 갖고 merge한다.
    # 이때 날씨 정보의 merge 기준 시간 형태는 2017-01-01 09:00:00
    # 이와 같은 형식을 갖도록 departTime을 time열로 수정한다.
    df2.rename(columns = {'departTime' : 'time'}, inplace = True)
    # 시간 형태 변경
    df2['time'] = pd.to_timedelta(df2['time'] + ':00') + df2['date']
    # 분 날리기
    df2['time'] = df2.time.dt.round('H')
    # weather_processed.csv를 로드하고 merge하기
    df_weather = pd.read_csv('./weather_processed.csv')
    df_weather['time'] = pd.to_datetime(df_weather['time'], format='%Y-%m-%d %H:%M:%S')
    df2 = pd.merge(left=df2, right=df_weather, how='left', on=['time'], sort=False)
    df2 = df2.drop(['Unnamed: 0', 'time', 'date', 'reason'], axis=1)

    # 9.
    df2.loc[(df2.state == '지연'), 'state'] = 1
    df2.loc[(df2.state == '출발'), 'state'] = 0
    # 열 순서 바꾸기
    df2 = df2[['airline', 'togo', 'passengers', 'weather', 'state', 'delayedTime']]
    
    df_statistics = df_statistics.append(df, ignore_index=True)
    df_ml = df_ml.append(df2, ignore_index=True)

# 500번 운항 미만 나라 컷
df_statistics = df_statistics[df_statistics.groupby('togo')['togo'].transform('count').ge(500)]
df_togo = df_statistics['togo'].to_frame().drop_duplicates()
# 취한 나라 리스트
togo_list = df_togo['togo'].values.tolist()
df_ml = df_ml.loc[df_ml['togo'].isin(togo_list)]
df_statistics.to_csv('./statistics_data.csv')
df_ml.to_csv('./ml_data.csv')
df_togo.to_csv('./togo_data.csv')
