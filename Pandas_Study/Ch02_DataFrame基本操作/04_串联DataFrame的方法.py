import pandas as pd


pd.options.display.max_rows = 8
student_list = pd.read_csv("./students_list.csv")

# 1>使用isnull方法将每个值转变为布尔值
print(student_list.isnull().head())
print(type(student_list.isnull().head()))

# 2>使用sum统计布尔值，返回的是Series
print(student_list.isnull().sum().head())
print(type(student_list.isnull().sum()))

# 3>对这个Series再次使用sum，返回整个DaraFrame的缺失值个数，返回值是个标量
print(student_list.isnull().sum().sum())
print(type(student_list.isnull().sum().sum()))

# 4>判断整个DataFrame上是否有缺失值，方法是连着使用两个any
print(student_list.isnull().any().any())
print(type(student_list.isnull().any().any()))

# 5>isnull返回同样大小的DataFrame，但所有的值变为布尔值
print(student_list.isnull())

# 6>student_list数据集的对象数据包含缺失值。默认条件下，聚合方法min、max、sum不会
# 返回任何值。
print(student_list["初试成绩"].max())  # 但是此处max、min、sum显示了结果
print(student_list["初试成绩"].isnull().sum())

# 7>填补缺失值
print(student_list["初试成绩"].fillna(432).max())

