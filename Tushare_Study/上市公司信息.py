import os
from os import path
import tushare as ts
import pandas as pd


# 初始化tushare程序包
token = "3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f"
ts.set_token(token)
pro = ts.pro_api()

# 设置文件存储位置
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
excel_path = d + "/上市公司基本信息.xlsx"

# 获取数据体
df1 = pro.stock_company(exchange="SSE",
                       fields="ts_code,chairman,manager,secretary,reg_capital,setup_date,province")

df2 = pro.stock_company(exchange="SZSE",
                       fields="ts_code,chairman,manager,secretary,reg_capital,setup_date,province")

# 一键填补缺失值、去重、重置索引函数


def fill_value(data):
    columns = data.columns
    for i in columns:
        data[i].fillna("无", inplace=True)
        num = data[i].isnull().sum()
        print(num)


fill_value(df1)
fill_value(df2)


writer = pd.ExcelWriter(excel_path)

df1.to_excel(writer, sheet_name="上交所公司信息", index=False)

df2.to_excel(writer, sheet_name="深交所公司信息", index=False)

writer.save()
