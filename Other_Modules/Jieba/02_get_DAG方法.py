"""
构建无向循环图
======================================
有向无环图，directed acyclic graphs，简称DAG，是一种图的数据结构，顾名思义，
就是没有环的有向图。jieba采用了Python的dict结构，可以更方便的表示DAG。最终的
DAG是以{k : [k , j , ..] , m : [m , p , q] , ...}的字典结构存储，其中k和m
为词在文本sentence中的位置，k对应的列表存放的是文本中以k开始且词sentence[k: j + 1]
在前缀词典中的 以k开始j结尾的词的列表，即列表存放的是sentence中以k开始的可能的词语
的结束位置，这样通过查找前缀词典就可以得到词。
get_DAG(self, sentence)函数进行对系统初始化完毕后，会构建有向无环图。
"""
import jieba


text = "今天晚上我吃了热干面"
DAG_list = jieba.get_DAG(text)
print(DAG_list)
print("/".join(jieba.cut(text, cut_all=False, HMM=False)))
print("/".join(jieba.cut(text, cut_all=True, HMM=False)))
