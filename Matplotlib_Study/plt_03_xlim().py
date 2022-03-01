import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)  # numpy.random.rand(x)用于返回一个或一组
# 服从“0-1”均匀分布的随机样本值。随机样本取值范围为[0，1），不包括1

plt.scatter(x, y, label="scatter figure")

plt.legend()

plt.xlim(0.05, 10)  # 函数xlim（xmin, xmax）和ylim（）用于设置坐标轴的显示范围
# 参数【xmin】表示x轴上的最小值，【xmax表示x轴上的最大值】
plt.ylim(0, 1)

plt.show()



