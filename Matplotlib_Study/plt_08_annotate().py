import numpy as np
import matplotlib.pyplot as plt


"""该函数的功能是【添加图形内容细节的“指向型”注释文本】
调用签名：↓
plt.annotate(string, xy=(np.pi/2,1.0), xytext=((np.pi/2)+0.15, 1.5), weight="bold"
color="b",arrowprops=dict(arrowstyle="->"), connectionstyle="arc3", color="b"))

string: 图形内容的注释文本
xy： 被注释图形内容的位置坐标
xytext：注释文本的位置坐标
weight：注释文本的字体粗细风格
color：注释文本的字体颜色
arrowprops：指示被注释内容的箭头的属性字典
"""
x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="m", label="plot figure")

plt.legend()

plt.annotate("maximum",
             xy=(np.pi/2, 1.0),
             xytext=((np.pi/2)+1.0, 0.8),
             weight="bold",
             color="black",
             arrowprops=dict(arrowstyle="<-",  # 此箭头可调换方向，向右
                             # 是指向xy位置，向左是指向xytext位置
                             connectionstyle="arc3", color="black"))
                             # 此处连接风格只可以arc和arc3，其他数字如arc2
                             # 会报错
plt.show()
