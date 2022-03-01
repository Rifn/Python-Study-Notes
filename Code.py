import pandas as pd


def fill_code(your_list):
    list1 = []
    for i in your_list:
        num = "0"*(6-len(i)) + i
        list1.append(num)
    return list1


def catch_4f(your_list):
    list1 = []
    for i in your_list:
        num = i[0:4]
        list1.append(num)
    return list1


def catch_6f(your_list):
    list1 = []
    for i in your_list:
        num = i[0:6]
        list1.append(num)
    return list1


def catch_6b(your_list):
    list1 = []
    for i in your_list:
        num = i[-6:]
        list1.append(num)
    return list1


def gene_merge(df, val_1, val_2):
    name_1 = df.columns[val_1]
    name_2 = df.columns[val_2]
    df["merge"] = df[name_1] + df[name_2]
    return df


def net_list(your_list):
    list1 = []
    for i in your_list:
        list1.append(i)
    return list1

