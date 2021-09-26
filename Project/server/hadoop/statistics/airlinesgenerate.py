import pandas as pd
from pandas.io.parsers import read_csv

df = read_csv('./statistics_data.csv')

df_airline = df['airline'].drop_duplicates().reset_index(drop=True)
# print(df.head(4))
df_airline.rename(columns = {'airline': 'name'}, inplace=True)
# df.columns = ['airline', 'name']
df_airline.to_csv('./airlines.csv')