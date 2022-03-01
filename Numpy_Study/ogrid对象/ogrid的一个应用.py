import numpy as np


x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
# 这里的mask是一个300*300的多维数组（矩阵）
# mask里面的数值为True或者False

print(x * 2)  # 多维数组和一个数相加减乘除等于，其对应的每一个元素和这个数相加减乘除
print(x + y)  # c参见numpy中列向量和行向量的相加减
print(x - 150)
print((x - 150) ** 2 + (y - 150) ** 2)
