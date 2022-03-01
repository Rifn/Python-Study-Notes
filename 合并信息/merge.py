import pandas as pd
import openpyxl

industry = pd.read_csv("./industry.csv")
value = pd.read_csv("./value.csv")

industry["code1"] = industry["code1"].astype("str")
value["code2"] = value["code2"].astype("str")

list1 = industry["code1"]
list2 = []
for i in value["code2"]:
    list2.append(i)

result_list = []
value_list = value["总市值"]

num1 = 0
for x in list1:
    num = 0
    p = 0
    for y in list2:
        if x == y:
            num += 1
            p = list2.index(y)
    if num != 1:
        print("%s不在表2" % x)
        result_list.append("404")
    else:
        result_list.append(value_list[p])
        num1 += 1
print(num1)
print(result_list)

industry["总市值"] = result_list

print(industry)

# writer = pd.ExcelWriter("./result.xlsx", encoding="utf-8-sig")
# industry.to_excel(writer, "sheet1")
# writer.save()
print("=" * 20)
print("合并数据成功！\n已经保存为：result.xlsx")
print("=" * 20)
