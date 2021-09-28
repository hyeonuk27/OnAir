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
    under_30 = models.FloatField()
    # 10분 초과 30분 이하 출발확률
    under_60 = models.FloatField()
    # 30분 초과 출발확률
    over_60 = models.FloatField()
    # 지연률
    delay_rate = models.FloatField()
    # 평균 지연시간
    delay_time = models.IntegerField()
    # 결항률
    cancel_rate = models.FloatField()
'''

airlines = ['아시아나항공', '대한항공', '진에어', '티웨이항공', '에어서울', '중국동방항공', '중국남방항공', '제주항공', '독일항공', '프랑스항공', '유나이티드항공', '델타항공', '네덜란드항공', '에미레이트항공', '카타르항공', '아메리칸항공']


for airline in airlines:
    
    # 항공사 것만 조회
    # airline_filter = df[df['airline'] != '{airline.name}'].index
    airline_filter = df[df['airline'] != airline].index
    airlinedata = df.drop(airline_filter)
    # print(airlinedata.head())
    # airlinedata.to_csv(f'data_{airline}.csv')


    # 목적지 총 운항횟수
    total_flight = airlinedata.drop(columns=['state', 'date', 'reason', 'passengers','delayedTime']).groupby('arrival').count().reset_index()
    # total_flight = airlinedata.groupby(by=['airline'], as_index=False).count()
    # total_flight.set_index(['arrival']).reset_index()
    total_flight.rename(columns = {'airline' : 'total'}, inplace = True)
    # total_flight = pd.DataFrame(total_flight, columns=['total'])
    # print(total_flight.head())

    # 총 지연횟수
    d_filter = airlinedata[airlinedata['state'] != '지연'].index
    delay = airlinedata.drop(d_filter)
    delaytotal = delay.drop(columns=['date', 'reason', 'state', 'passengers', 'delayedTime']).groupby('arrival').count().reset_index()
    delaytotal.rename(columns = {'airline': 'delayed'}, inplace = True)
    # delaytotal = pd.DataFrame(delaytotal, columns=['total'])
    # print(delaytotal.head())
    merge_right = pd.merge(total_flight, delaytotal, on="arrival", how='right')

    # 총 결항횟수
    c_filter = airlinedata[airlinedata['state'] != '취소'].index
    cancel = airlinedata.drop(c_filter).reset_index(drop=True)
    print(cancel.head())
    cancel = cancel.drop(columns=['date', 'reason', 'state', 'passengers', 'delayedTime']).groupby('arrival').count().reset_index()
    cancel.rename(columns={'airline': 'canceled'}, inplace=True)
    print(cancel.head())


    merge_right = pd.merge(merge_right, cancel, on="arrival", how='right')
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
        c_30 = airlinedata['delayedTime'] <= 30
        under_30 = len(airlinedata[a & b & c_30])
        u30_list.append(under_30)


        # 1시간 이내 출발 
        c_31 = airlinedata['delayedTime'] > 30
        c_60 = airlinedata['delayedTime'] <= 60
        under_60 = len(airlinedata[a & b & c_31 & c_60])
        u60_list.append(under_60)


        # 1시간 초과 출발 
        c_61 = airlinedata['delayedTime'] > 60
        over_60 = len(airlinedata[a & b & c_61])
        o60_list.append(over_60)

    merge_right['under_30'] = u30_list
    merge_right['under_60'] = u60_list
    merge_right['over_60'] = o60_list


    # 평균지연시간
    avg_delay = airlinedata.drop(d_filter).reset_index(drop=True)
    avg_delay = avg_delay[['delayedTime', 'arrival']].groupby('arrival').mean().reset_index()
    # avg_delay = pd.DataFrame(avg_delay, columns=['delayedTime'])
    # print(avg_delay.head())


    # left
    merge_right = pd.merge(merge_right, avg_delay, on="arrival", how='left')
    # merge_right.to_csv('./right.csv')

    res = merge_right

    # 지연률
    res['delayedTime'] = round(res['delayedTime'])
    res['delayrate'] = round(res['delayed'] / res['total'] * 100, 2)

    # 결항률
    res['cancelrate'] = round(res['canceled'] / res['total'] * 100, 2)

    # 30분이내
    res['rateu30'] = round(res['under_30'] / res['total'] * 100, 2)
    res['rateu60'] = round(res['under_60'] / res['total'] * 100, 2)
    res['rateo60'] = round(res['over_60'] / res['total'] * 100, 2)

    res = res.drop(columns=['under_30', 'under_60', 'over_60', 'delayed', 'canceled'])
    res = res.assign(airline=f'{airline}')
    # print(res.head())
    # res.to_csv(f'./res_{airline}.csv')
    # pd.concat([final, res])



# final.to_csv('./final.csv')


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





    # df.loc[(df.togo == 'CEB()'), 'togo'] = 'CEB(세부)'
    # df.loc[(df.togo == 'IAD(워싱톤)'), 'togo'] = 'IAD(워싱턴)'
    # df.loc[(df.togo == 'BKK(수안나폼(방콕))'), 'togo'] = 'BKK(수완나품(방콕))'
    # df.loc[(df.togo == 'SGN(떤선녀엇(호찌민))'), 'togo'] = 'SGN(떤선녓(호치민))'
    # df.loc[(df.togo == 'HKT(푸껫)'), 'togo'] = 'HKT(푸켓)'
    # df.loc[(df.togo == 'TSN(천진)'), 'togo'] = 'TSN(톈진)'
    # df.loc[(df.togo == 'SYX(산야)'), 'togo'] = 'SYX(싼야)'
    # df.loc[(df.togo == 'YNT(연대)'), 'togo'] = 'YNT(연태)'
    # df.loc[(df.togo == 'ULN(부얀트 우카(울란바타르))'), 'togo'] = 'ULN(보얀트 오하(울란바토르))'
    # df.loc[(df.togo == 'KKJ(기타규슈)'), 'togo'] = 'KKJ(기타큐슈)'
    # df.loc[(df.togo == 'JHB(조호바루)'), 'togo'] = 'JHB(조호르바루)'
    # df.loc[(df.togo == 'VIE(비엔나)'), 'togo'] = 'VIE(빈)'
    # df.loc[(df.togo == 'JHB(조호바루)'), 'togo'] = 'JHB(조호르바루)'
    # df.loc[(df.togo == 'JHB(조호바루)'), 'togo'] = 'JHB(조호르바루)'