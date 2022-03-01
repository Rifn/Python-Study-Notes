import pandas as pd


def remove_first(your_list):
    list1 = []
    for i in your_list:
        num = i[1] + i[2] + i[3] + i[4] + i[5] + i[6]
        list1.append(num)
    return list1


result = pd.read_csv("./result.csv")

result["code1"] = remove_first(result["code1"])

writer = pd.ExcelWriter("./result.xlsx", encoding="utf-8-sig")
result.to_excel(writer, "sheet1")
writer.save()
