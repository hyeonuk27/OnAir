import pandas as pd

############## 항공사, 목적지, 총 운항횟수, 총 지연횟수, 총 결항횟수, 평균지연시간, 지연사유별개수

# 첫번째 컬럼을 index로 사용
df = pd.read_csv('./statistics_data.csv', index_col=0)

'''
class StatisticsResult(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    # 목적지
    arrival = models.CharField(max_length=50)
    # 항공사
    airline = models.CharField(max_length=20)
    # 목적지에 대한 총운항횟수
    total = models.IntegerField()
    # 10분내 출발확률
    under_10 = models.FloatField()
    # 10분 초과 30분 이하 출발확률
    under_30 = models.FloatField()
    # 30분 초과 출발확률
    over_30 = models.FloatField()
    # 지연률
    delay_rate = models.FloatField()
    # 평균 지연시간
    delay_time = models.IntegerField()
    # 결항률
    cancel_rate = models.FloatField()

'''
airlines = ['아시아나항공', '대한항공', '진에어', '티웨이항공', '에어서울', '중국동방항공', '중국남방항공', '제주항공', '독일항공', '프랑스항공', '유나이티드항공', '델타항공', '네덜란드항공', '에미레이트항공', '카타르항공', '아메리칸항공']
# 항공사 것만 조회
# airline_filter = df[df['airline'] != '{airline.name}'].index
airline_filter = df[df['airline'] != '대한항공'].index
airlinedata = df.drop(airline_filter).reset_index(drop=True)
# print(airlinedata.head())


# 목적지 총 운항횟수
total_flight = airlinedata.drop(columns=['state', 'date', 'reason', 'passengers','delayedTime']).groupby('arrival').count()
# total_flight = airlinedata.groupby(by=['airline'], as_index=False).count()
total_flight.rename(columns = {'airline' : 'total'}, inplace = True)
print(total_flight.head(5))


# 총 지연횟수
d_filter = airlinedata[airlinedata['state'] != '지연'].index
delay = airlinedata.drop(d_filter).reset_index(drop=True)
delaytotal = delay.drop(columns=['date', 'reason', 'state', 'passengers', 'delayedTime']).groupby('arrival').count()
delaytotal.rename(columns = {'airline': 'delayed'}, inplace = True)
# print(delaytotal.head())


# 10분 이내 출발
# a = airlinedata['arrival'] == '{arrival.name}'
a = airlinedata['arrival'] == 'PEK(베이징)'
b = airlinedata['state'] != '취소'
c_10 = airlinedata['delayedTime'] <= 10
under_10 = len(airlinedata[a & b & c_10])
# print(under_10)


# 30분 이내 출발
c_11 = airlinedata['delayedTime'] > 10
c_30 = airlinedata['delayedTime'] <= 30
under_30 = len(airlinedata[a & b & c_11 & c_30])
# print(under_30)


# 30분 초과 출발
c_31 = airlinedata['delayedTime'] > 30
over_30 = len(airlinedata[a & b & c_31])
# print(over_30)


# 총 결항횟수
c_filter = airlinedata[airlinedata['state'] != '취소'].index
cancel = airlinedata.drop(c_filter).reset_index(drop=True)
cancel = cancel.drop(columns=['date', 'reason', 'state', 'passengers', 'delayedTime']).groupby('arrival').count()
cancel.rename(columns={'airline': 'canceled'}, inplace=True)
# print(cancel.head())


# 평균지연시간
avg_delay = airlinedata.drop(d_filter).reset_index(drop=True)
avg_delay = avg_delay['delayedTime'].groupby(airlinedata['arrival']).mean()
avg_delay = pd.DataFrame(avg_delay, columns=['delayedTime'])
# print(avg_delay.head())


##### 목적지 따로 지정해야 함 ->
# 지연사유별 개수
reason_group = airlinedata.drop(d_filter).reset_index(drop=True)
# arrival_filter = df[df['arrival'] != '{arrival_name}'].index
arrival_filter = reason_group[reason_group['arrival'] != 'LAX(로스앤젤레스)'].index
reason_group = reason_group.drop(arrival_filter).reset_index(drop=True)
reason_group = reason_group.drop(columns=['date', 'arrival', 'passengers', 'state'])
reason_count = reason_group.groupby('reason').count()

# 지연사유별 평균지연시간
reason_avg = reason_group.groupby(by=['reason'], as_index=False).mean()
reason_count.rename(columns = {'airline' : 'total'}, inplace = True)
reason_count = reason_count.sort_values(by=['total'], ascending=False)

# print(reason_count.head())
# print(reason_avg.head())





