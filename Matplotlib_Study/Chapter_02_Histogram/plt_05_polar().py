import numpy as np
import matplotlib.pyplot as plt

"""
函数功能： 在极坐标轴上绘制折线图
调用签名：plt.polar(theta, r)
theta：每个标记所在射线与极径的夹角
r：每个标记到原点的距离
"""

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)  # 第四个参数代表不包含末尾值
r = 30*np.random.rand(barSlices)

plt.polar(theta, r,
          color="chartreuse",  # "表重用", chartreuse代表黄绿色
          linewidth=2,
          marker="*",
          mfc="k",  # Maybe, "mfc" means " marker's front color".
          ms=20)  # "ms" means "marker's size".

plt.show()

print(theta)
print(r)
