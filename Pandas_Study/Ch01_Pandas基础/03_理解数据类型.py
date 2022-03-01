import pandas as pd


filepath = "students_list.csv"
students_list = pd.read_csv(filepath)  # 读取csv文件

# 各列的类型
print(students_list.dtypes)

# 显示各类型的数量
students_list.get_dtype_counts()  # TODO(白) 这段代码运行会报错，解决它！

