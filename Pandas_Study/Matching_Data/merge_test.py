import pandas as pd


def fill_code(your_list):
    list1 = []
    for val in your_list:
        num = "0" * (6-len(val)) + val
        list1.append(num)
    return list1


df_code = pd.read_csv("./code.csv")
df_stata = pd.read_csv("./stata.csv")

df_code["code"] = df_code["code"].astype("str")
df_stata["Symbol"] = df_stata["Symbol"].astype("str")
df_code["code"] = fill_code(df_code["code"])
df_stata["Symbol"] = fill_code(df_stata["Symbol"])

print(df_code)
print(df_stata)

merge = pd.merge(df_code, df_stata, how="left", left_on="code", right_on="Symbol")
print(merge)

merge.to_excel("./result.xlsx", sheet_name="result", index=False)