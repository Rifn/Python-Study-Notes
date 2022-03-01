import pandas as pd
import numpy as np


student_list = pd.read_csv("./students_list.csv")
print(student_list.head())  # 这是原来的列的顺序

print(student_list.columns)  # 打印出列名的columns

# 将索引按照指定的顺序排列
disc_core = ['初试成绩', '政治', '外国语', '业务课一', '业务课二', '初试成绩']
disc_other = ['序号', '专业', '考生编号', '姓名', '专项计划', '是类别', '学习方式',
              '复试成绩', '总成绩（按百分制折算）', '是否拟录取']
new_col_order = disc_core + disc_other
print(set(student_list.columns) == set(new_col_order))  # 判断新的列名列表和
# 原columns格式是否一致，值得注意的是，只要某个列名在原来的列名中，即使一个列名重
# 复多次，输出结果也为 True ，但若添加额外的列名如【坂井泉水】，则程序会报错

stu2 = student_list[new_col_order]  # 设置新的列名之后，DataFrame从15列扩充到了16列
print((stu2.head()))
