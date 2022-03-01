import numpy as np
import os
from os import path
from wordcloud import WordCloud
from imageio import imread


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

stopwords_path = d + "/wc_cn/stopwords_cn_en.txt"
print(stopwords_path)

font_path = "/fonts/BlackoakStd.otf"
font_path = d + font_path
print(font_path)

image_address1 = d + "/wc_cn/LuXun.jpg"
image_address2 = d + "/wc_cn/LuXun_colored.jpg"
print(image_address1)
print(image_address2)

print(path.join(d, d + '/wc_cn/CalltoArms.txt'))
