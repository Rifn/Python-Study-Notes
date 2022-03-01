import pandas as pd


filepath = "students_list.csv"
student_list = pd.read_csv(filepath)

# print(student_list.shape)
# student_list2 = student_list.set_index("student_tittle")
# print(student_list2)

# 通过index_col参数命名
student_list3 = pd.read_csv(filepath, index_col="student_tittle")
# 上述代码报错可能是因为此pandas版本较低
pass
