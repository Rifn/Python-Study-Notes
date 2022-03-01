# -*- coding:utf-8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/5/27'
# 邮箱：fonttian@163.com
# CSDN：http://blog.csdn.net/fontthrone

import sys
import jieba
from os import path
import os


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text_path = "/txt_file/精神无囚笼.txt"
stopwords_path = "/txt_file/停用词表2750.txt"  # 这里可以直接加【./】
text = open(path.join(d, d + text_path), encoding="utf-8").read()
# print(text)
stopwords = open(path.join(d, d + stopwords_path), encoding="utf-8").read()
# print(stopwords)

# def jiebaclearText(text):

mywordlist = []
seg_list = jieba.cut(text, cut_all=False)
liststr = "/ ".join(seg_list)
# f_stop = open(path.join(d, d + stopwords_path), encoding="utf-8")


f_stop_seg_list = stopwords.split("\n")  # 将停用词表转换为一个停用词列表形式
print(f_stop_seg_list)



