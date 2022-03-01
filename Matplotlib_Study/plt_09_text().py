import numpy as np
import matplotlib.pyplot as plt


"""
该函数的功能是【添加图形内容细节的“无指向型”注释文本】
调用签名：↓
plt.text(x, y, string, weight="bold", color="b")
x: 注释文本内容所在位置的横坐标。
y：注释文本内容所在位置的纵坐标。【经本人测试】，这个xy坐标指的是文本标签左上角的坐标
string：注释文本内容。
weight：注释文本内容的粗细风格。
color：注释文本内容的字体颜色。
"""
x = np.linspace(0.05, 10, 1000)
u = np.sin(x)

plt.plot(x, u, ls="-", lw=2, c="c", label="plot figure")

plt.legend()

plt.text(3.10, 0.1, "y=sin(x)", weight="bold", color="b")

plt.show()

print(np.sin(3.10))
