import numpy as np
import matplotlib.pyplot as plt


"""
函数功能：标示不同图形的文本标签图例
调用签名：plt.legend(loc="lower left")
loc: 图例在图中的地理位置
"""
x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls=":", lw=2, c="c", label="plot figure")

# plt.legend(loc="lower left")  # 这个括号内的loc参数加和不加绘图似乎无差异，
# # 可能本来只有legend()的时候，参数默认值就是现在写这个，改了参数可能会有变化的

plt.show()
