import pandas as pd


filepath = "students_list.csv"
students_list = pd.read_csv(filepath)  # 读取csv文件

pd.set_option("max_rows", 10)

# 1>访问【姓名】这一列
print(students_list["姓名"])

# 2>也可以通过属性的方式选取
print(students_list.姓名)
"""
python对象的属性名竟然可以使用中文，甚至，对象名也可以使用中文,这里把csv对象
“students_list”命名成“学生名单”竟然也是可以的，程序正常运行。
可以通过pycharm的【refactor】功能查看一种命名是否有效
"""

# 3>查看序列的类型
print(type(students_list["姓名"]))

# 4>查看选取列的名字
xm = students_list["姓名"]
print(xm.name)

# 5>单列Series转换为DataFrame
xm.to_frame()
print(xm.to_frame().head())  # to_frame()方法将这个序列转换为DataFrame的数据格式，
# head()方法显示前几行，head()方法是有返回值的，事实证明，不加to_frame()也是可以直接让这
# 个叫xm的Series直接调用head()方法的
print(type(xm.to_frame()))  # 虽然输出结果一样，但是这个xm.to_frame()已经
# 是一个实实在在的dataframe类型
