import pandas as pd


pd.options.display.max_rows = 8
student_list = pd.read_csv("./students_list.csv")

# 1>打印行数和列数
print("\n1>打印行数和列数：\n", "=" * 15)
print(student_list.shape)
print(type(student_list.shape))

# 2>打印数据的个数
print("\n2>打印数据的个数：\n", "=" * 15)
print(student_list.size)
print(type(student_list.size))

# 3>该数据的维度
print("\n3>该数据的维度：\n", "=" * 15)
print(student_list.ndim)
print(type(student_list.ndim))

# 4>该数据集的长度
print("\n4>该数据集的长度：\n", "=" * 15)
print(len(student_list))  # 数据集长度等于index的长度
print(type(len(student_list)))

# 5>各个列的值的个数
print("\n5>各个列的值的个数：\n", "=" * 15)
print(student_list.count())  # 都等于index的长度
print(type(student_list.count()))  # 各个列值的个数与最小值返回的都是Series数据类型

# 6>各个列的最小值
print("\n6>各个列的最小值：\n", "=" * 15)
print(student_list.min())
print(type(student_list.min()))

# 7>打印描述信息
print("\n7>打印描述信息：\n", "=" * 15)
print(student_list.describe())
print(type(student_list.describe()))  # 描述信息返回的是DataFrame数据类型

# 8>使用percentiles参数指定分位数
pd.options.display.max_rows = 10
print("\n8>使用percentiles参数指定分位数：\n", "=" * 15)
print(student_list.describe(percentiles=[.01, .3, .99]))
print(type(student_list.describe(percentiles=[.01, .3, .99])))

# 9>打印各列空值的个数
pd.options.display.max_rows = 8
print("\n9>打印各列空值的个数：\n", "=" * 15)
print(student_list.isnull().sum())
print(type(student_list.isnull().sum()))  # 返回一个序列
print(type(student_list.isnull()))  # 返回与原DataFrame的shape一样大小的一个数据表


# 10>设定skipna=False，没有缺失值的数值列才会计算结果
print("\n10>设定skipna=False，没有缺失值的数值列才会计算结果：\n", "=" * 15)
print(student_list.min(skipna=False))
