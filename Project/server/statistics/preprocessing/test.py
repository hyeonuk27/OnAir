import pandas as pd

airlines = ['아시아나항공', '대한항공', '진에어', '티웨이항공', '에어서울', '중국동방항공', '중국남방항공', '제주항공', '독일항공', '프랑스항공', '유나이티드항공', '델타항공', '네덜란드항공', '에미레이트항공', '카타르항공', '아메리칸항공']




df = pd.read_csv('./statistics_data.csv', index_col=0)
df = df.drop(columns=['date', 'reason', 'arrival', 'passengers'])
df = df.fillna(0)



u30f = df[df['delayed_time'] <= 30].index
u30 = df.drop(u30f).reset_index(drop=True)
u30 = u30.groupby('airline').count()
print('u30', u30)

x = df['delayed_time'] > 30
y = df['delayed_time'] <= 60
u60 = df[x & y]
u60 = u60.groupby('airline').count()
print('u60', u60)

z = df[df['delayed_time'] > 60].index
o60 = df.drop(z).reset_index(drop=True)
o60 = o60.groupby('airline').count()
print('o60', o60)

    # print(df.head())
    # airline_filter = df[df['airline'] != airline].index
    # airlinedata = df.drop(airline_filter)
    # # 30분 이내 출발 
    # b = df['state'] != '취소'
    # c_30 = df['delayed_time'] <= 30
    # under_30 = len(df[b & c_30])

    # # 1시간 이내 출발 
    # c_31 = df['delayed_time'] > 30
    # c_60 = df['delayed_time'] <= 60
    # under_60 = len(df[b & c_31 & c_60])


    # # 1시간 초과 출발 
    # c_61 = df['delayed_time'] > 60
    # over_60 = len(df[b & c_61])

    # late_list.append([airline, under_30, under_60, over_60])