import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.5, 3.5, 100)  # 表示在0.5到3.5之间平局地取100个数
# print(x)
i = 0
j = 0
print(x)
print(type(x))

while i < 100:
    print(i+1, end="  ")
    print(x[j])
    i += 1
    j += 1

