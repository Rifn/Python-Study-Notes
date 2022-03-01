import tushare as ts
import pandas as pd


token = "3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f"
ts.set_token(token)
pro = ts.pro_api()

df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001',
                   fields='exchange,cal_date,is_open, pretrade_date', is_open='0')

print(df)
# ts.get_hist_data("600808", "2020-01-01", "2020-10-31", "D", "3")
