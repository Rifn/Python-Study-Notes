from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import os
from os import path
from PIL import Image


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
print("这是当前地址(d)：" + d)

text = open(path.join(d, "constitution.txt")).read()
print("text文本加载成功！")

ring_image = Image.open(path.join(d, "ring_mask.png"))
print("这是mask图片信息：", end="'")
print(ring_image)

plt.figure()
plt.imshow(ring_image)
plt.show()
print("mask图片显示成功!")

ring_mask = np.array(ring_image)
print(ring_mask)

text2 = "success"
wc = WordCloud(font_path=None, mask=ring_mask, max_words=200,
               background_color="white", repeat=True)
wc.generate(text2)

plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.show()
