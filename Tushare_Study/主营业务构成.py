import pandas as pd
import tushare as ts


token = "3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f"
ts.set_token(token)
pro = ts.pro_api()

df = pro.fina_mainbz(ts_code="600808.SSE", tpye="P")
print(df)
