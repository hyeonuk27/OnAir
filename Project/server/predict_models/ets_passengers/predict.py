import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing as HWES
from sklearn.metrics import mean_squared_error as MSE 
from sklearn.metrics import mean_absolute_error as MAE


def predict(airline):
    df = pd.read_csv('./%s.csv' % airline, index_col='date', parse_dates=True)
    df = df.drop(['Unnamed: 0', 'index'], axis=1)
    # 결측치 보간 필요
    df = df.resample('M').first()
    df = df.interpolate(method='time')
    df_train = df.iloc[:-3]
    df_test = df.iloc[-3:]

    # 주석 처리는 테스트해 본 결과 의미가 크지 않은 모델들
    # fit1 = SimpleExpSmoothing(df_train).fit()
    # fit2 = Holt(df_train).fit()
    fit3 = Holt(df_train, exponential=True).fit()
    # fit4 = Holt(df_train, damped_trend=True).fit()
    fit5 = Holt(df_train, exponential=True, damped_trend=True).fit()
    # fit6 = HWES(df_train, seasonal_periods=12, trend='add', seasonal='add').fit(optimized=True, use_brute=True)
    # fit7 = HWES(df_train, seasonal_periods=12, trend='add', seasonal='mul').fit(optimized=True, use_brute=True)

    # forecast_1 = fit1.forecast(8)
    # forecast_2 = fit2.forecast(8)
    forecast_3 = fit3.forecast(3)
    # forecast_4 = fit4.forecast(8)
    forecast_5 = fit5.forecast(3)
    # forecast_6 = fit6.forecast(8)
    # forecast_7 = fit7.forecast(8)

    def MAPE(y_test, y_pred): 
        y_test, y_pred = np.array(y_test), np.array(y_pred)
        return np.mean(np.abs((y_test - y_pred) / y_test)) * 100

    # MAPE 비교표
    # def eval_all(y_test, y_pred, model): 
    #     mape = MAPE(y_test, y_pred)
    #     return [mape]
    #
    #
    # eval_all_df = pd.DataFrame( 
    #     {
    #     # 'SES': eval_all(df_test, forecast_1, fit1), 
    #     # "Holt's": eval_all(df_test, forecast_2, fit2), 
    #     'Exponential': eval_all(df_test, forecast_3, fit3), 
    #     # 'Trend_Add': eval_all(df_test, forecast_4, fit4), 
    #     'Trend_Mult': eval_all(df_test, forecast_5, fit5), 
    #     # 'Trend_Season_Add': eval_all(df_test, forecast_6, fit6), 
    #     # 'Trend_Season_Mult': eval_all(df_test, forecast_7, fit7)
    #     } , 
    #     index=['MAPE'])

    if MAPE(df_test, forecast_3) < MAPE(df_test, forecast_5):
        return Holt(df, exponential=True).fit().forecast(3).values
    else:
        return Holt(df, exponential=True, damped_trend=True).fit().forecast(3).values


# print(predict('티웨이항공'))