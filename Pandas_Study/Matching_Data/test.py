import pandas as pd


# df = pd.DataFrame({})
# list1 = ["600808", "600809"]
# df["code"] = list1
# print(df)
# help(pd.DataFrame)

list1 = ["中国", "America", "Japan", "England"]
list2 = ["Japan", "England"]

list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)
