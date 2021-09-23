import pandas as pd
import glob

airline_set = {
    '중국남방항공', 
    '중국동방항공', 
    '델타항공', 
    'KLM네덜란드항공', 
    '대한항공', 
    '카타르항공', 
    '아메리칸항공', 
    '아시아나항공', 
    '루프트한자 독일항공', 
    '에미레이트항공', 
    '캐나다항공', 
    '유나이티드항공', 
    '에어 프랑스',
    '진에어',
    '티웨이항공',
    '제주항공',
    '에어서울'
}

all_data = pd.DataFrame()

for f in glob.glob("./*.xlsx"):
    year, month = f.replace('By_Airline_', '')[2:6], f.replace('By_Airline_', '')[6:8]
    date = year + '-' + month
    df = pd.read_excel(f)
    # 엑셀의 첫 행이 의미 없음
    df = pd.read_excel(f, skiprows=[0])
    # 항공사명이 Unnamed: 0, 인천 공항에서 출발하는 이용객 수가 출발.1이라는 열 이름을 갖고 있다.
    new_df = pd.DataFrame(df.iloc[1:], columns=['Unnamed: 0', '출발.1'])
    # 칼럼 이름 변경
    new_df = new_df.rename(columns={'Unnamed: 0': 'airline', '출발.1': 'passengers'})
    # airline_set에 있는 항공사 데이터만
    con = new_df['airline'].isin(airline_set)
    condition_df = new_df.loc[con]
    condition_df.insert(0, 'date', [date] * condition_df.shape[0])
    condition_df['date'] = pd.to_datetime(condition_df['date'])
    
    all_data = all_data.append(condition_df, ignore_index=True)

# passengers는 이용객수이지만, 현재 float로 소수점 첫째자리가 0으로 나온다. 해당 열의 type을 int로 바꿔준다.
all_data['passengers'] = all_data['passengers'].astype(int)
# 항공사 별로 묶기
groups = all_data.groupby(all_data.airline)
# 각 항공사 이름으로 csv 파일 만들기
for airline in airline_set:
    group = groups.get_group(airline)
    # 0인 값 제거
    condition_not_zero = group[group['passengers'] == 0].index
    group = group.drop(['airline'], axis=1).drop(condition_not_zero).sort_values(by=['date'], axis=0).reset_index(drop=True)
    group.to_csv('./%s.csv' % airline)