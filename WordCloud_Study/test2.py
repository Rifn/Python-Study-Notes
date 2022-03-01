import os
from os import path
import matplotlib.pyplot as plt
import numpy as np


print(path)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
print(d)

print(locals())

address = path.join(d, "constitution")
print(address)
