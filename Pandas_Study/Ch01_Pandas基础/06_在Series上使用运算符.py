import pandas as pd


pd.options.display.max_rows = 6

filepath = "./students_list.csv"
student_list = pd.read_csv(filepath)
st_name = student_list["姓名"]
first_score = student_list["初试成绩"]
print(first_score)

# 1>每列值加1
print(first_score + 1)

# 2>每列值乘以2.5
print(first_score * 2.5)

# 3>每列值除以7之后的商
print(first_score // 7)  # 求余运算符是“%”

# 4>判断是否大于376
print(first_score > 376)

# 5>判断是否等于字符串
print(st_name == "何依格")

# 6>利用通用函数实现加法
print(first_score.add(1))

# 7>利用通用函数实现乘法
print(first_score.mul(2.5))

# 8>利用通用函数实现底除
print(first_score.floordiv(7))

# 9>利用通用函数实现是否大于的判断
print(first_score.gt(376))

# 10>利用通用函数实现是否等于的判断
print(st_name.eq("何依格"))

# 11>利用通用函数实现取模
print(first_score.mod(5))  # 取模也即求余

# 12>通过序列的类型对象来创建新的序列
a = type(1)  # 此处a是int类型对象，注意int对象和int类型对象是不同的
print(a(2.000))
print(type(a))
print(type(1))
a = type(first_score)  # 此处a是pandas.core.series.Series类型对象
print(a([1, 2, 3]))  # 将列表[1，2，3]以a这个类型(序列类型)来呈现，a等于一个类型对象
print(type(a))
print(type(a([1, 2, 3])))  # 这就对了！nice！
