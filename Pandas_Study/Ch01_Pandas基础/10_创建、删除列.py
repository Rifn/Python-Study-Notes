import pandas as pd


filepath = "students_list.csv"
student_list = pd.read_csv(filepath)

# 1>通过列名添加新列
student_list["备注"] = 0
print(student_list.columns)

# 2>给新列赋值
student_list["备注"] = student_list["政治"] + student_list["外国语"]
print(student_list["备注"])  # 上述命令将备注列赋值为政治和外国语成绩之和

# 3>用all()检查是否所有的布尔值都为True
first_score = student_list["初试成绩"]
student_list["judge_score"] = student_list["初试成绩"] >= student_list["备注"]
judge_score = student_list["judge_score"]
print(judge_score.all())  # 因为本人初试成绩在csv文件中为空，所以judge_score序列有一个False

# 4>用insert()方法原地插入列
public_score_index = student_list.columns.get_loc("外国语") + 1
print(public_score_index)  # 这里用get_loc()方法得到的是一个整数，代表新列位置
student_list.insert(public_score_index, column="公共课",
                    value=student_list["政治"] + student_list["外国语"])
'''插入列的方法输入参数依次为：1>插入地址；2>插入列的列名；3>插入列的值
其中，地址可以直接写数字，但这样也有缺点。列名可以直接写入字符串，也可
加一个column=。列值也可以加value=,方便阅读代码。'''
print(student_list.head())
