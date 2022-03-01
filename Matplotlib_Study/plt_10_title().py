import numpy as np
import matplotlib.pyplot as plt


"""
函数功能：添加图形内容的标题
调用签名：plt.title(string)
string: 图形内容的标题文本
"""
x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")

plt.legend()

plt.title("y=sin(x)")

plt.show()
