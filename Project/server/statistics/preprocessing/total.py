import pandas as pd

############## 항공사, 총 운항, 총 지연횟수, 총 결항횟수, 지연평균시간, 지연사유별개수

# 첫번째 컬럼을 index로 사용
df = pd.read_csv('./statistics_data.csv', index_col=0)

# 전체적으로 쓸모없는 열 삭제
df = df.drop(columns=['date', 'passengers'])

# 총 운항 (항공사 전체)
total_flight = df.drop(columns=['reason', 'state', 'delayedTime']).groupby('airline').count()
# total_flight = df.groupby(by=['airline'], as_index=False).count()
total_flight.rename(columns = {'arrival' : 'total'}, inplace = True)
# print(total_flight.head(5))

# 총 지연개수
d_filter = df[df['state'] != '지연'].index
delay = df.drop(d_filter).reset_index(drop=True)
delay = delay.drop(columns=['reason', 'state', 'delayedTime']).groupby('airline').count()
delay.rename(columns = {'arrival': 'delayed'}, inplace = True)
# print(delay.head())

# 총 결항개수
c_filter = df[df['state'] != '취소'].index
cancel = df.drop(c_filter).reset_index(drop=True)
cancel = cancel.drop(columns=['reason', 'state', 'delayedTime']).groupby('airline').count()
cancel.rename(columns={'arrival': 'cancel'}, inplace=True)
# print(cancel.head())

# 지연평균시간 (----)
avg_delay = df.drop(d_filter).reset_index(drop=True)
avg_delay = avg_delay['delayedTime'].groupby(df['airline']).mean()
avg_delay = pd.DataFrame(avg_delay, columns=['delayedTime'])
# print(avg_delay.head())

# 지연사유별개수 (항공사별로 빼야함)
reason_group = df.drop(d_filter).reset_index(drop=True)
reason_group = reason_group.drop(columns=['arrival', 'state', 'delayedTime'])
print(reason_group.head())
reason_group = reason_group.assign(cnt=1)
reason_group = reason_group.groupby(by=['airline', 'reason'], as_index=False).sum()
# reason_avg = reason_group.groupby(by=['reason'], as_index=False).mean()
# reason_group.rename(columns = {'airline' : 'total'}, inplace = True)
# reason_group = reason_group.sort_values(by=['airline'], ascending=False)
# print(reason_group.head())

reason_group.to_csv('../reasoncount.csv')

