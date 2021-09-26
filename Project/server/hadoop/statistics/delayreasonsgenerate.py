import pandas as pd
from pandas.io.parsers import read_csv

df = read_csv('./statistics_data.csv')
df_reason = df['reason'].value_counts()

df_reason.to_csv('./delay_reasons.csv')