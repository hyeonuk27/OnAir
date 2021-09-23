import pandas as pd
from pandas.io.parsers import read_csv

df = read_csv('./weather.csv')
# 필요 없는 열 삭제
df = df.drop([
    'dt', 'timezone', 'city_name', 'lat', 'lon', 'temp', 'feels_like', 'temp_min' , 'temp_max', 'pressure', 'sea_level', 'grnd_level', 'humidity', 
    'wind_deg', 'rain_1h', 'rain_3h', 'snow_1h', 'snow_3h', 'clouds_all', 'weather_id', 'weather_description', 'weather_icon'
    ], axis=1)
# 풍속이 13이 넘으면 weather_main을 Typhoon으로 수정
df['wind_speed'] = df['wind_speed'].astype(float)
df.loc[(df.wind_speed > 13.0), 'weather_main'] = 'Typhoon'
df = df.drop(['wind_speed'], axis=1)
# 시간대를 우리나라 시간으로 바꾸기
df.rename(columns = {'dt_iso' : 'time', 'weather_main' : 'weather'}, inplace = True)
df['time'] = pd.to_datetime(df['time'].str.replace(' UTC', ''), format='%Y-%m-%d %H:%M:%S %z')
dt_time = pd.DatetimeIndex(df['time'])
dt_time = dt_time.tz_convert('Asia/Seoul')
# 형식 바꾸기
df['time'] = dt_time.strftime('%Y-%m-%d %H:%M:%S')
df.to_csv('./weather_processed.csv')