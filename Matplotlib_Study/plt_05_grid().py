import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

plt.grid(linestyle=":", color="y")  # 此处线条风格可以简写ls，线条颜色可以简写c

plt.show()
