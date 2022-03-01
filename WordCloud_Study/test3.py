import matplotlib.pyplot as plt
import numpy as np


x, y = np.ogrid[:300, :300]
mask = abs(x-150) + abs(y-150) > 150
mask = mask.astype(int)
plt.figure()
plt.imshow(mask, interpolation="bilinear")
plt.axis("off")
plt.show()