# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

"""
函数功能：在y轴上绘制定性数据的分布特征
调用签名：plt.barh(x, y)
x: 标示在y轴上的定性数据的类别
y: 每种定性数据的类别的数量
"""

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 用来显示中文标签
mpl.rcParams["axes.unicode_minus"] = False  # 用来显示负号

# 定义一些简单的数据 some simple data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# 创建水平柱形图 create bar
plt.barh(x, y, align="center", color="c", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"],
         hatch="/")

# 设置坐标轴标签 set x,y_axis label
plt.xlabel("箱子重量(kg)")
plt.ylabel("箱子编号")

plt.show()
