from os import path
import os
import jieba.analyse as analyse

import matplotlib.pyplot as plt


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
print(d)

text_path = "/txt_file/精神无囚笼.txt"
print(path.join(d, d + text_path))

text = open(path.join(d, d + text_path), encoding="utf-8").read()
print(text)

i = 1
for key in analyse.extract_tags(text, 5, withWeight=False):
    # analyse.extract_tags()方法的返回值是一个关键词列表<class 'list'>

    num = "这是第%d个关键词:" % i
    print(num + key)
    i += 1
print(analyse.extract_tags(text, 20, withWeight=False))
print(type(analyse.extract_tags(text, 20, withWeight=False)))


