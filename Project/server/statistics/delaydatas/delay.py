import pandas as pd

df = pd.read_csv('./statistics_data.csv', index_col=0)
df = df.drop(columns=['passengers'])

airlines = ['아시아나항공', '대한항공', '진에어', '티웨이항공', '에어서울', '중국동방항공', '중국남방항공', '제주항공', '독일항공', '프랑스항공', '유나이티드항공', '델타항공', '네덜란드항공', '에미레이트항공', '카타르항공', '아메리칸항공']

u30_list = list()
u60_list = list()
o60_list = list()

# 전체 지연 사유 분포
for airline in airlines: 
    airline_filter = df[df['airline'] != airline].index
    airlinedata = df.drop(airline_filter)
    airlinedata['reason']= airlinedata['reason'].replace(['에 의한 지연'],['기타'])
    # airlinedata.to_csv('./test.csv')


    delay_filter = airlinedata[airlinedata['state'] != '지연'].index
    delaydata = airlinedata.drop(delay_filter)
    total_delay = delaydata.groupby('reason').count().reset_index()
    total_delay = total_delay.drop(columns=['date', 'airline', 'arrival', 'delayed_time'])
    total_delay = total_delay.sort_values(by=['state'], ascending=False)
    # print(total_delay.head())

# 30, 60, 60 

    # 30분 이내 출발 
    b = airlinedata['state'] != '취소'
    c_30 = airlinedata['delayed_time'] <= 30
    under_30 = len(airlinedata[b & c_30])
    u30_list.append([airline, under_30])

    # 1시간 이내 출발 
    c_31 = airlinedata['delayed_time'] > 30
    c_60 = airlinedata['delayed_time'] <= 60
    under_60 = len(airlinedata[b & c_31 & c_60])
    u60_list.append([airline, under_60])


    # 1시간 초과 출발 
    c_61 = airlinedata['delayed_time'] > 60
    over_60 = len(airlinedata[b & c_61])
    o60_list.append([airline, over_60])

# 월별 평균 출발시간
    monthly_delay = airlinedata
    monthly_delay['date'] = monthly_delay['date'].str[:7]
    monthly_delay = monthly_delay.groupby(['date'], as_index=False).mean().groupby('date')['delayed_time'].mean().reset_index()
    # print(monthly_delay.head())

# 목적지별 지연 사유 분포
    arrival_filter = delaydata[delaydata['arrival'] != 'KOJ(가고시마)'].index
    arrivals_data = delaydata.drop(arrival_filter)
    arrivals_delay_reason = arrivals_data.groupby(['reason'], as_index=False).size().reset_index()
    arrivals_delay_reason = arrivals_delay_reason.sort_values(by=['size'], ascending=False)
    arrival_delay_list = arrivals_delay_reason['reason'].values.tolist()[:6]
    # print(arrivals_delay_reason.head())
    # print('list:', arrival_delay_list)
    
# 지연사유별 평균 지연시간
    arrivals_delay = arrivals_data.groupby(['arrival', 'reason'], as_index=False).mean().reset_index()
    arrivals_delay = arrivals_delay.sort_values(by=['delayed_time'], ascending=False)
    # print(arrivals_delay)


