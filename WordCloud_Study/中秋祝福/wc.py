import os
from os import path
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from imageio import imread
from WordCloud_Study.中秋祝福 import gen_txt

mask = np.array(imread("./4乐.png"))

text = gen_txt.mid_autumn_txt()[3]


def jieba_processing_text(text):
    # jieba.add_word("朱亚男")
    jieba.add_word("好吗")
    jieba.add_word("好的")
    jieba.add_word("化云化烟")
    mywordlist = []
    seg_list = text.split()
    liststr = "/".join(seg_list)

    stop_word = ["只不过", "这个", "时而", "只有", "人才"]

    for myword in liststr.split("/"):
        if len(myword) > 1 and myword not in stop_word:
            mywordlist.append(myword)
    return " ".join(mywordlist)


wc = WordCloud(font_path="./思源黑体CN-Light.otf",
               mask=mask, background_color="white", color_func=lambda *args,
               **kwargs: (100, 100, 100), max_words=200)
wc.generate(jieba_processing_text(text))

wc.to_file("./乐.png")

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()
