import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")

plt.legend()

plt.axhline(y=0.0, c="r", ls="--", lw=2)  # h代表horizontal，水平的
plt.axvline(x=4.0, c="r", ls="-", lw=2)  # v代表vertical， 垂直的
# y，x表示参考线出发点

plt.show()
