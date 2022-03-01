import pandas as pd


def catch6f(your_list):
    list1 = []
    for i in your_list:
        list1.append(i[0:6])
    return list1


def catch6b(your_list):
    list1 = []
    for val in your_list:
        num = val[-6:]
        list1.append(num)
    return list1


df1 = pd.read_csv("./info.csv")
df2 = pd.read_csv("./value.csv")

df1["ts_code"] = catch6f(df1["ts_code"])
df2["代码"] = catch6b(df2["代码"])
# print(df1)
# print(df2)
merge = pd.merge(df1, df2, how="left", left_on="ts_code", right_on="代码")
print(df1)
print(merge)

