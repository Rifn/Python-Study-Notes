import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 用来显示中文标签
mpl.rcParams["axes.unicode_minus"] = False  # 用来显示负号
plt.figure(figsize=(5, 5), dpi=80)

x1 = np.linspace(0, 1, 100)
y1 = x1 * 1
x2 = np.linspace(0, 0.95, 30)
y2 = - np.sqrt(1-np.square(x2)) + 1
y3 = - np.sqrt(1-np.square(x1)) + 1

plt.plot(x1, y1, ls="-", lw=1, c="black", label="绝对平等线")
plt.plot(x1, y3, ls=":", lw=1, c="black", label="拟合的洛伦兹曲线")
plt.scatter(x2, y2, c="black", label="企业营业收入占比")

plt.legend()

# plt.axis("equal")
plt.xlim(0, 1)  # 设置坐标轴显示范围
plt.ylim(0, 1)

plt.xlabel("企业数量的百分比")  # plt.xlabel(string)
plt.ylabel("营业收入的百分比")  # 设置横纵坐标轴名称

plt.text(0.6, 0.33, "A", fontsize=20, c="black", weight="bold", color="b")  # 设置注释标签
plt.text(0.8, 0.15, "B", fontsize=20, c="black", weight="bold", color="b")

plt.draw()
plt.savefig("./基尼系数.png", dpi=3000)

plt.show()
plt.close()
