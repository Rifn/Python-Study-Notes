# -*-coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 用来显示中文标签
mpl.rcParams["axes.unicode_minus"] = False  # 用来显示负号

"""
函数功能：在x轴上绘制箱体的定量数据输入值
调用签名：plt.hist()
x: 在x轴上绘制箱体的定量数据输入值
"""

# 设置测试结果 set test scores
boxWeight = np.random.randint(0, 10, 10)  # 从0到10中随机取10个数，不含10

x = boxWeight  # 这是所观测样本组的各项数值

# 绘制直方图 plot histgram
bins = range(0, 11, 1)  # 此处bins显示了x轴的分组情况，从a到b，不含b，range()的第三个参数
# 代表了组距，也可直接把range()插入到plt.hist()的参数中,但那样对阅读代码不友好

plt.hist(x, bins=bins,
         color="g",  # 颜色
         histtype="bar",
         rwidth=1,  # 柱子宽度，一般设为1
         alpha=1,  # 透明度
         hatch="/")  # 填充：可选选项

# 设置x，y轴标签 set x,y-axis label
plt.xlabel("箱子重量（kg）")
plt.ylabel("箱子个数（个）")

plt.show()

# print(x)
# print(bins)
