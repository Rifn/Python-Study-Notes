import pandas as pd


filepath = "students_list.csv"
students_list = pd.read_csv(filepath)  # 读取csv文件

# 1>查看Series所有不重复的指令
s_attr_methods = set(dir(pd.Series))
print(len(s_attr_methods))  # 那本中文参考手册上是442个不重复的指令，
# 这里423个兴许是因为pandas版本较低

# 2>查看DataFrame所有不重复的指令
df_attr_methods = set(dir(pd.DataFrame))
print(len(df_attr_methods))  # 那份中文参考手册上DataFrame不重复指令有445个

# 3>这两个集合中有多少共有的指令
print(len(s_attr_methods & df_attr_methods))  # 中文参考手册--》376个

# 4>选取姓名和初试成绩两列
st_name = students_list["姓名"]
first_score = students_list["初试成绩"]

# 5>查看头部
print(st_name.head())
print(first_score.head())  # 这两个head()方法都是有返回值的

# 6>分别计数
pd.set_option("max_rows", 8, "max_columns", 3)  # 此句代码仅对之后的打印显示有效
print(st_name.value_counts())  # 序列的计数方法也是有返回值的,返回值也是一个序列
# print(type(st_name.value_counts()))
# print(type(st_name))
print(first_score.value_counts())
print(st_name.size)  # 查看st_name序列中的数据规模
print(st_name.shape)  # 查看st_name序列中的数据体形状
print(len(st_name))   # 查看st_name序列中的数据长度

# 7>st_name序列有多少非空值
print(st_name.count())  # 要注意序列的count()方法是查看非空值，value_counts()方法计数
print(first_score.count())  # 查看first_score序列有多少非空值

# 8>查看中位分位数
print(first_score.quantile(0.75), "第30名的初试成绩刚好386分")
# print(st_name.quantile()) # 此句代码运行会报错

# 9>求最小值、最大值、平均值、中位数、标准差、总和
a = [first_score.min(), first_score.max(), first_score.mean(), first_score.median(),
     first_score.std(), first_score.sum()]
print(a)

# 10>打印描述信息
print(first_score.describe())
print(st_name.describe())

# 11>分位数方法的一些拓展
print(first_score.quantile(.2))  # 这是序列的20%分位数
print(first_score.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))  # 各十分之一分位数

# 12>非空值
print(st_name.isnull())

# 13>填充缺失值
# print(first_score.isnull())
print(first_score.count(), "这是将本人分数去掉之后的初试成绩序列实值个数")
first_score_filled = first_score.fillna(378)
print(first_score_filled.count(), "这是填补之后的实值个数")
# print(first_score.value_counts())
# print(first_score_filled.value_counts())

# 14>删除缺失值
first_score_dropped = first_score.dropna()
print(first_score_dropped.size)

# 15>value_counts(normalize)方法返回计数频率
print(first_score.value_counts(normalize=True))

# 16>判断是是否有缺失值
print(first_score.hasnans)
print(first_score.notnull())
