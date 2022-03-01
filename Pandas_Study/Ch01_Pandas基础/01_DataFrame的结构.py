import pandas as pd


# 1>设定最大列数和行数
pd.set_option("max_columns", 8, "max_rows", 10)  # 从该代码之后的print()出的数据遵从此格式

# 2>用read_csv()方法读取csv文件
filepath = "./students_list.csv"  # TODO(白) 解决文件地址的问题（将调用数据放在统一文件夹时候该如何书写地址以实现对数据文件的调用）
students_list = pd.read_csv(filepath)

# 3>head()方法可以查看前五行，head(n)可以查看前n行
print(students_list.head(30))

# 4>Pandas的DataFrame数据类型是一个【pandas.core.frame.DataFrame】类
print(type(students_list))

for i in students_list.columns:
    series = students_list[i]
    series.fillna(378, inplace=True)
    x = series.isnull().sum()
    print(x)

students_list.to_excel("./student.xlsx", sheet_name="Sheet1")
