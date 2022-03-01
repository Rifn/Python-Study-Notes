import pandas as pd


def fill(your_list):
    # 将序列中的股票代码补全为六位的方法
    list1 = []
    for i in your_list:
        if len(i) == 6:
            num1 = i
            list1.append(num1)
        else:
            num2 = ("0"*(6-len(i))) + i
            list1.append(num2)
    return list1


def add(your_list):
    list1 = []
    for i in your_list:
        num = "x" + i
        list1.append(num)
    return list1


def catch6(your_list):
    list1 = []
    for i in your_list:
        num = i[2] + i[3] + i[4] + i[5] + i[6] + i[7]
        list1.append(num)
    return list1


industry = pd.read_csv("industry111.csv")
value = pd.read_csv("./value.csv")


industry["code1"] = industry["code1"].astype("str")
industry["code1"] = add(fill(industry["code1"]))

print(industry["code1"])

print(industry.dtypes)
print(industry["code1"])

# industry.to_csv("./industry.csv", index=False)

value["code2"] = value["code2"].astype("str")
value["code2"] = add(catch6(value["code2"]))
print(value["code2"])

# value.to_csv("./value.csv", index=False)
