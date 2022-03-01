import pandas as pd


filepath = "students_list.csv"
students_list = pd.read_csv(filepath)  # 读取csv文件

# 1>提取列索引
columns = students_list.columns
print(columns)
print(students_list.columns)  # 两种方法都可以，可以视 colunmns为对象的属性

# 2>提取行索引
index = students_list.index
print(index)

# 3>提取数据
data = students_list.values
print(data)

# 4>index的类型
print(type(index))

# 5>columns的类型
print(type(columns))

# 6>data的类型
print(type(data))

# 7>判断是不是子类型
print(issubclass(pd.RangeIndex, pd.Index))

# 8>访问index的值
print(index.values)
print(index.values[0])  # index的值是一个列表，所以可以索引或者切片

# 9>访问columns的值
print(columns.values)  # columns的值也是一个列表，也可以索引或者切片
print(columns.values[2])
