import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
from os import path

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

o = np.array([0, 0, 0])  # 圆心坐标
R = 1  # 圆的直径为1
h = np.arange(-R, R, 0.0001)        # 把高度按0.0001进行采样
r = np.sqrt(R-h**2)  # 每个小圆对应的半径r
theta = np.arange(0, 2*np.pi, 0.01)  # 取样间隔0.01
x = np.outer(np.cos(theta), r)+o[0]  # 和每个小圆的半径进行外积得到每个小圆的x坐标，每个高度对应一个小圆的x
y = np.outer(np.sin(theta), r)+o[1]  # 和每个小圆的半径进行外积得到每个小圆的y坐标，每个高度对应一个小圆的y
z = np.outer(np.ones(len(theta)), h)+o[2]  # 和高度进行外积得到每个小圆的z坐标
ax.plot_surface(x, y, z, cmap=plt.get_cmap('rainbow'))  # 绘制球体

plt.show()  # 展示画板
