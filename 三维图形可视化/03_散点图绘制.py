import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl


mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )

    with each number distributed Uniform(vmin, vmax).
    """
    pass
    return (vmax - vmin) * np.random.rand(n) + vmin

plt.show()
