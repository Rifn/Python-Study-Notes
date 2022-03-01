import pandas as pd


filepath = "students_list.csv"
student_list = pd.read_csv(filepath)

st_name = student_list["姓名"]
first_score = student_list["初试成绩"]

# 1>value_counts().head(3),计数 查看前三行一起使用
print(st_name.value_counts().head(3))
print(first_score.value_counts().head(3))

# 2>统计缺失值的数量
print(first_score.isnull().sum())

# 3>显示first_score的数据类型
print(first_score.dtype)

# 4>确实值填充为0、转换为整型、查看前五
print(first_score.fillna(0).astype(int).head())

# 5>缺失值的比例
print(first_score.isnull().mean())

# 6>使用括号串联
print((first_score.fillna(0).astype(int).head()))
