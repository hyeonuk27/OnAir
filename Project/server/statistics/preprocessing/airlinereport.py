import pandas as pd

############## 항공사, 목적지, 총 운항횟수, 총 지연횟수, 총 결항횟수, 평균지연시간, 지연사유별개수
airlines = ['아시아나항공', '대한항공', '진에어', '티웨이항공', '에어서울', '중국동방항공', '중국남방항공', '제주항공', '독일항공', '프랑스항공', '유나이티드항공', '델타항공', '네덜란드항공', '에미레이트항공', '카타르항공', '아메리칸항공']

import random, string

def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))

# 첫번째 컬럼을 index로 사용
df = pd.read_csv('./statistics_data.csv', index_col=0)

for airline in airlines:
    
    # 항공사 것만 조회
    # airline_filter = df[df['airline'] != '{airline.name}'].index
    airline_filter = df[df['airline'] != airline].index
    airlinedata = df.drop(airline_filter)
    # print(airlinedata.head())
    # airlinedata.to_csv(f'data_{airline}.csv')


    # 목적지 총 운항횟수
    total_flight = airlinedata.drop(columns=['state', 'date', 'reason', 'passengers','delayed_time']).groupby('arrival').count().reset_index()
    # total_flight = airlinedata.groupby(by=['airline'], as_index=False).count()
    # total_flight.set_index(['arrival']).reset_index()
    total_flight.rename(columns = {'airline' : 'total'}, inplace = True)
    # total_flight = pd.DataFrame(total_flight, columns=['total'])
    # print(total_flight.head())

    # 총 지연횟수
    d_filter = airlinedata[airlinedata['state'] != '지연'].index
    delay = airlinedata.drop(d_filter)
    delaytotal = delay.drop(columns=['date', 'reason', 'state', 'passengers', 'delayed_time']).groupby('arrival').count().reset_index()
    delaytotal.rename(columns = {'airline': 'delayed'}, inplace = True)
    # delaytotal = pd.DataFrame(delaytotal, columns=['total'])
    # print(delaytotal.head())
    merge_right = pd.merge(total_flight, delaytotal, on="arrival", how='left')

    # 총 결항횟수
    c_filter = airlinedata[airlinedata['state'] != '취소'].index
    cancel = airlinedata.drop(c_filter).reset_index(drop=True)
    # print(cancel.head())
    cancel = cancel.drop(columns=['date', 'reason', 'state', 'passengers', 'delayed_time']).groupby('arrival').count().reset_index()
    cancel.rename(columns={'airline': 'canceled'}, inplace=True)
    # print(cancel.head())


    merge_right = pd.merge(merge_right, cancel, on="arrival", how='left')
    # merge_right.to_csv(f'./right_{airline}.csv')

    arrival_list = merge_right['arrival'].tolist()
    # print(arrival_list)
    u30_list = list()
    u60_list = list()
    o60_list = list()

    for arrival in arrival_list:

        # 30분 이내 출발 
        # a = airlinedata['arrival'] == '{arrival.name}'
        a = airlinedata['arrival'] == arrival
        b = airlinedata['state'] != '취소'
        c_30 = airlinedata['delayed_time'] <= 30
        under_30 = len(airlinedata[a & b & c_30])
        u30_list.append(under_30)


        # 1시간 이내 출발 
        c_31 = airlinedata['delayed_time'] > 30
        c_60 = airlinedata['delayed_time'] <= 60
        under_60 = len(airlinedata[a & b & c_31 & c_60])
        u60_list.append(under_60)


        # 1시간 초과 출발 
        c_61 = airlinedata['delayed_time'] > 60
        over_60 = len(airlinedata[a & b & c_61])
        o60_list.append(over_60)

    merge_right['under_30'] = u30_list
    merge_right['under_60'] = u60_list
    merge_right['over_60'] = o60_list


    # 평균지연시간
    avg_delay = airlinedata[['delayed_time', 'arrival']].groupby('arrival').mean().reset_index()
    # avg_delay = pd.DataFrame(avg_delay, columns=['delayed_time'])
    print(avg_delay.head())


    # left
    merge_right = pd.merge(merge_right, avg_delay, on="arrival", how='left')
    # merge_right.to_csv('./right.csv')

    res = merge_right
    # print(res.head())

    # 지연률
    res['delayed_time'] = round(res['delayed_time'])
    res['delayrate'] = round(res['delayed'] / res['total'] * 100, 2)

    # 결항률
    res['cancelrate'] = round(res['canceled'] / res['total'] * 100, 2)

    res = res.fillna(0)

    res['under_30'] = round(res['under_30'] / (res['total'] - res['canceled']) * 100, 2)
    res['under_60'] = round(res['under_60'] / (res['total'] - res['canceled']) * 100, 2)
    res['over_60'] = round(res['over_60'] / (res['total'] - res['canceled']) * 100, 2)

    res = res.drop(columns=['delayed', 'canceled'])
    res = res.assign(airline=f'{airline}')
    
    # id
    id = [ make_random_id() for _ in range(len(res)) ]
    res['id'] = id

    # nan->0
    res = res.fillna(0)

    # print(res.columns)
    res.rename(columns={'delayed_time': 'delay_time', 'delayrate': 'delay_rate', 'cancelrate': 'cancel_rate'}, inplace=True)
    res.to_csv(f'./res_{airline}.csv')

    ##### 목적지 따로 지정해야 함 ->
    # 지연사유별 개수
    reason_group = airlinedata.drop(d_filter).reset_index(drop=True)
    arrival_filter = reason_group[reason_group['arrival'] != 'LAX(로스앤젤레스)'].index
    reason_group = reason_group.drop(arrival_filter).reset_index(drop=True)
    reason_group = reason_group.drop(columns=['date', 'arrival', 'passengers', 'state'])
    reason_count = reason_group.groupby('reason').count().reset_index()
    reason_count = reason_count.drop(columns=['delayed_time'])
    reason_count.rename(columns = {'airline' : 'total'}, inplace = True)

    # 지연사유별 평균지연시간
    reason_avg = reason_group.groupby(by=['reason'], as_index=False).mean().reset_index()
    reason_avg.rename(columns = {'airline' : 'avg_time'}, inplace = True)
    reason_avg['delayed_time'] = round(reason_avg['delayed_time'], 2)
    # reason_avg = reason_avg.sort_values(by=['avg_time'], ascending=False)

    merge_chart = pd.merge(reason_count, reason_avg, on="reason", how='left')
    merge_chart = merge_chart.drop(columns=['index'])

    # merge_chart.to_csv('./delaychart.csv')





