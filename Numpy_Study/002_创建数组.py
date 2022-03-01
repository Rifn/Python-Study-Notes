import numpy as np


# np.arange()方法
a = range(1, 20)  # range 的返回值为一个迭代器
b = np.arange(1, 20)  # 而 np.arange 的返回值是一个左闭右开的数组
print(a, b)

# np.array(),该种创建数组的方法应是最常见的，具体任务中更多是转出的数据 df.to_numpy()
nd = np.array([1, 2, 3, 4, 3, 5])
print(type(nd))
print(nd)
print(np.array(range(1, 10, 2)))  # 等价于 np.arange(1, 10, 2)

# 创建 0 元素数组
print(np.zeros((5, 5)))  # 参数 (5, 5) 代表的目标组的形状（shape），即5行5列的数组
# 创建 1 元素数组
print(np.ones((5, 5)))

# 创建相同元素数组
print(np.full((3, 5), 2))

# 用 np.random()生成随机数组
rand = np.random.RandomState(30)
array5 = rand.randint(0, 100, [3, 5])
print(array5)

print(array5.shape)  # 数组的形状，几行几列
print(type(array5.shape))
print(array5.dtype)  # 数组中元素的数据类型
print(type(array5.dtype))
print(np.zeros((5, 5)))
print(np.zeros(shape=(5, 5), dtype=np.int))
