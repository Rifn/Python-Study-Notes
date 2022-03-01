import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm as cm

# 定义数据 define data
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# 绘制曲线图形 plot figure
plt.plot(x, y, ls="--", lw=2, label="plot figure")

# 绘制离散图形 scatter figure
plt.scatter(x, y1, c="0.25", label="scatter figure")

# 清理一些东西（去除图中无关紧要的元素）
# some clean up( removing chartjunk)
# 去掉上部和右部的框线 turn the top spine and the right spine off
for spine in plt.gca().spines.keys():
    if spine == "top" or spine == "right":
        plt.gca().spines[spine].set_color("none")

# 设置x轴和y轴的取值范围 set x,y axis limit
plt.xlim(0.0, 4.0)
plt.ylim(-3.0, 3.0)

# 设置坐标轴标签  set axes labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# 设置网格线 set x,y axis grid
plt.grid(True, ls=":", color="r")

# 添加一条平行于x轴的水平参考线 add a horizontal line across the axis
plt.axhline(y=0.0, ls="--", lw=2, c="r")

# 添加一块垂直于x轴的垂直参考区域 add a vertical span across the axis
plt.axvspan(xmin=1.0, xmax=2.0, facecolor="y", alpha=0.3)

# 对图形内容细节，添加“指向型”注释文本信息 set annotating info
plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+0.15, 1.5), weight="bold",
             color="r", arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b")
             )
plt.annotate("spines", xy=(0.75, -3), xytext=(0.35, -2.25), weight="bold", color="b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b")
             )
plt.annotate("", xy=(0, -2.78), xytext=(0.4, -2.32),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))
plt.annotate("", xy=(3.5, -2.98), xytext=(3.6, -2.70),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))

# 对图形内容细节，添加“无指向型”注释文本信息 set text info
plt.text(3.6, -2.70, "'|'is tickline", weight="bold", color="b")
plt.text(3.6, -2.95, "3.5 is ticklable", weight="bold", color="b")

# 设置标题 set title
plt.title("structure of matplotlib")

# 绘图
plt.legend()

plt.show()
