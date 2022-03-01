import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


x = np.linspace(-10, 10, 1000)
y = (x-7)*(x-7)-5

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 用来显示中文标签
mpl.rcParams["axes.unicode_minus"] = False  # 用来显示负号

for spine in plt.gca().spines.keys():
    if spine == "top" or spine == "right":
        plt.gca().spines[spine].set_color("none")

plt.plot(x, y, ls="-", lw=2, label="函数g(x)")

plt.legend()

plt.axhline(y=0.0, c="k", ls="-", lw=2)  # h代表horizontal，水平的
plt.axvline(x=0.0, c="k", ls="-", lw=2)  # v代表vertical， 垂直的

plt.annotate("",
             xy=(5, 0),
             xytext=(7, 50),
             weight="bold",
             color="black",
             arrowprops=dict(arrowstyle="<-",  # 此箭头可调换方向，向右
                             # 是指向xy位置，向左是指向xytext位置
                             connectionstyle="arc3", color="black"))
                             # 此处连接风格只可以arc和arc3，其他数字如arc2
                             # 会报错

plt.show()
