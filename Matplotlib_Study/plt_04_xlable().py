import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")  # 这里的【c】
# 是颜色参数

plt.legend()

plt.xlim(0.05, 10)
plt.ylim(-1, 1)
plt.xlabel("x-axis")  # plt.xlabel(string)
plt.ylabel("y-axis")

plt.show()
