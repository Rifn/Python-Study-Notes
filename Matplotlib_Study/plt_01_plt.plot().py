import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.05, 10, 1000)
y = np.cos(x)

plt.plot(x, y, ls="-", c="black", lw=2, label="plot figure")

plt.legend()
plt.show()
