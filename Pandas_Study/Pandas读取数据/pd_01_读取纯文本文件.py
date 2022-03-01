import pandas as pd


filepath = "./test.csv"  # 将需要读取的文件的地址先赋给一个变量，方便后续，
# 此处【.】代表脚本当前所在文件夹

day_tem = pd.read_csv(filepath)  # 调用签名：pd.read_csv(path),其中path变量
# 是需要读取文件的地址，这里将文件读取后赋给一个对象，方便后续对数据文件的分析和处理

# 查看前几行数据
head = day_tem.head()  # head方法可以查看前五行，加参数n可以查看前n行
print("1.这是前几行")
print(head)


# 查看数据的形状，返回（行数，列数）
shape = day_tem.shape
print("2.这是形状")  # 值得注意的是，这里的表头是不算在形状里面的
print(shape)

# 查看列名列表
columns = day_tem.columns
print("3.这是列名列表")
print(columns)  # TODO(neo):解决CSV文件中为什么会有一个"unnamed"表头
print(columns.values)
# 以上问题已解决：用excel打开csv文件，删除空白的第三列

# 查看索引列
index = day_tem.index
print("4.这是查看索引列")
print(index)
print(index.values)

# 查看数据体
data = day_tem.values
print("5.这是查看数据体")
print(data)

# 查看每列的数据类型
datatype = day_tem.dtypes
print("6.这是查看每列的数据类型")
print(datatype)

# 查看pandas一些组件的类型
type_idx = type(index)  # index的类型
type_clm = type(columns)  # columns的类型
type_data = type(data)  # data的类型
judge = issubclass(pd.RangeIndex, pd.Index)  # 判断是不是子类型

print("7.", type_idx)
print("8.", type_clm)
print("9.", type_data)
print("10.", judge)
