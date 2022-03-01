import math
import cmath  # 这个“cmath”是python中一个专门用来处理复数的一个模块
import matplotlib


print(round(3.5))
print(math.floor(32.9))
print(int(32.9))
bai = math.floor  # 此处可以用变量来引用函数，这时函数不用加"()"，
# 直接用“bai” 就可以使用函数
print(bai(3.5))
print(cmath.sqrt(-1))

# 赋值语句
x = 3
y = 6
print("赋值语句", "="*20)
print(x, y)
# 交换两个变量值的方法
print("交换变量", "="*20)
z = x  # 1>用第三个变量的方法
x = y
y = z
print(x, y)

x, y = y, x  # 2>python中独有的交换变量方法(适用于列表元素互换等问题)，此外还有
# “利用运算规律法”和“异或运算”法等等
print(x, y)

# 列表元素交换
print("列表元素交换", "="*20)
list1 = [1, 2, 3, 4]
print(list1)
list1[0], list1[3] = list1[3], list1[0]
print(list1)
list1[0], list1[3] = list1[3], list1[0]
print(list1)

