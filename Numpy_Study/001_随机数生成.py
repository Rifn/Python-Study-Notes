import random
import numpy as np


print(random.randint(1, 5))  # 生成区间内一个整数，右侧可取到
print(random.uniform(1, 10))  # 生成 1-10 之间的随机浮点数
print(round(random.uniform(1, 10), 2))


"""
1>通过np.random.RandomState定义一个随机变量的生成器rand
2>根据目标数组的特征（如服从均匀分布还是正态分布），选择生成器rand提供的具体方法，如
  rand.ranint(), rand.rand(), rand.randn()
"""
rand = np.random.RandomState(32)  # 生成整数，如生成一个3*6的矩阵，矩阵的每个元素取值范围为[1,10]
x = rand.randint(0, 10, (3, 6))
print(type(x))
print(x)

# 生成服从均匀分布的浮点数（实数）数组，如生成一个含有5个元素的数组
rand = np.random.RandomState(1)
y = rand.rand(5) * 10  # rand.rand()的返回值的取值范围为[0,1], 在此“*10”的目的是“调整
# 所生成随机数的取值范围”
print(y)
print(rand.rand(5))
print(rand.rand(6, 5) * 10)

# 生成服从正态分布的浮点数（实数）数组，如生成一个含有5个元素且服从正态分布的数组
rand = np.random.RandomState(1)
z = rand.randn(5) + 5  # 此处加 5 的含义为改变正太分布的均值
print(z)

# 生成等距数列，如产生一个含有 20 个元素的等距数列，其中每个元素的取值范围为 [0, 10]
lin = np.linspace(0, 10, 20)
print(lin)
help(np.linspace)





