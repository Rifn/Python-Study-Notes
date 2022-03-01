import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

z = x + y

ax.plot(x, y, z, label="00")
plt.show()
