import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("expand_frame_repr", False)

# 设置tolken
token = "3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f"
ts.set_token(token)
pro = ts.pro_api()

# 导入000002.SZ前复权日线行情数据，保留收盘价列
df = ts.pro_bar(ts_code="000002.SZ", adj="qfq")
