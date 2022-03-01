# -*- coding:utf-8 -*-
import os
from os import path
import tushare as ts
import pandas as pd

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
excel_path = d + "/信息.xlsx"

token = "3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f"
ts.set_token(token)
pro = ts.pro_api()

df1 = pro.stock_company(exchange="SSE",
                       fields="ts_code,chairman,manager,secretary,reg_capital,setup_date,province")
# print(df1)

columns = df1.columns
print(columns)

# 查看和填补缺失值
for i in columns:
    series = df1[i]
    # print(series)
    series.fillna(0, inplace=True)
    x = series.isnull().sum()
    print(x)

df1.to_excel('winner.xlsx', index=False)

# 去重
df1.drop_duplicates(inplace=True)

# 重新设置索引
df1.reset_index(inplace=True, drop=True)

# 保存为excel文件
df1.to_excel(excel_path, index=False)



