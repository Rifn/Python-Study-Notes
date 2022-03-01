import pandas as pd
import numpy as np


pd.options.display.max_columns = 40

student_list = pd.read_csv("./students_list.csv")

# 1>用列表选取多个列
student_score = student_list[["姓名", "初试成绩", "复试成绩"]]  # 这里输入参数看作一个列表
# 这样选取多列之后的student_score也是一个DataFrame类型，你可以print其类型查看。
# 而如果只选取一列的话，那么其类型(class)就是pandas中的Series类型
print("\n1>用列表选取多个列:\n===================")
print(student_score.head())

print(type(student_score))
print(type(student_list))

# 2>选取单列
print("\n2>选取单列:\n===================")
print(student_list[["姓名"]].head())
print(type(student_list["姓名"]))
print(type(student_list[["姓名"]]))  # 通过列表来选取单独一列时数据为DataFrame类型

# 3>将列表赋值给一个变量，便于多选
cols = ["姓名", "初试成绩", "复试成绩"]
print("\n3>将列表赋值给一个变量便于多选:\n=======================")
print(student_list[cols].head())

# 4>使用select_dtypes(),选取整数列
a = student_list.select_dtypes(include=["int"]).head()  # 这个include=可以省略
print("\n4>选取整数列:\n===================")
print(a)

# 5>选取所有的数值列
print("\n5>选取所有数值列：\n====================")
print(student_list.select_dtypes(include=["number"]).head())

# 6>通过filter()函数过滤选取多列
print("\n6>过滤选取多列：\n===================")
print(student_list.filter(like="成绩").head())
print(type(student_list.filter(like="成绩")))  # filter之后的数据对象也是DateFrame

# 7>通过正则表达式选取多列
# 正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，
# 组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
print("\n7>通过正则表达式选取多列：\n===================")
print(student_list.filter(regex="试").head())  # TODO(neo): 学会正则表达式
print(type(student_list.filter(regex="试")))  # 正则表达式之后的数据对象也是DataFrame

# 8>filter()函数，传递列表到参数items，选取多列
print("\n8>filter()函数，传递列表到参数items，选取多列: \n=====================")
print(student_list.filter(items=["初试成绩", "坂井泉水"]).head())
# 这个items列表参数中和DataFrame列名列表中重合的那个(些)列，将会被选取到
# 这种方法尽管只选取了一列，其选取的数据对象也是DataFrame
print(type(student_list.filter(items=["初试成绩", "坂井泉水"])))
