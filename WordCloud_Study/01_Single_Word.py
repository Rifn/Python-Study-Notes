import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "square open open open square back"

x, y = np.ogrid[:300, :300]  # 参见Numpy>ogrid

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2  # 这里的mask是一个300*300的多维数组（矩阵）
mask2 = abs(x-150) + abs(y-150) < 150  # 这一段代码生成一个菱形的mask
# 可参见numpy中的列向量和行向量相加等
# mask里面的数值为True或者False
print(mask[150, 150])

mask = 255 * mask.astype(int)  # 这里将多维数组中的bool值元素【True】变为整数1，【False】为0
print(mask[150, 150])  # TODO(neo)：解决这里参数改为225等值mask变为方形的问题


wc = WordCloud(background_color="white", repeat=True, mask=mask)
wc.generate(text)

plt.axis("off")  # 设置不显示坐标轴
plt.imshow(wc, interpolation="bilinear")  # 失去这行代码，虽然会显示一个Figure，但是为空内容
plt.show()  # 没有这行代码，词云没法显示


