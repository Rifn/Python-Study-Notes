import pandas as pd
from Code import *


df_code = pd.read_csv("./code.csv")
df_stata = pd.read_csv("./stata.csv")

df_code["code"] = df_code["code"].astype("str")
df_stata["Symbol"] = df_stata["Symbol"].astype("str")

df_code["code"] = fill_code(df_code["code"])
df_stata["Symbol"] = fill_code(df_stata["Symbol"])

anti_list = []
code_list = net_list(df_code["code"])
stata_list = net_list(df_stata["Symbol"])
for i in stata_list:
    if i not in code_list:
        anti_list.append(i)

anti_code = pd.DataFrame({})
anti_code["code"] = anti_list
anti_code.drop_duplicates("code", keep="first", inplace=True)
print(anti_code)
#
df_stata2 = df_stata.drop_duplicates("Symbol", keep="first", inplace=False)
print(df_stata2["Symbol"])
merge = pd.merge(anti_code, df_stata, how="left", left_on="code", right_on="Symbol")
merge.to_excel("./result2.xlsx", sheet_name="result2", index=False)
