"""
cut()分词方法
=====================
jieba分词有三种模式：全模式、精确模式、搜索引擎模式。全模式和精确模式通过
jieba.cut实现，搜索引擎模式对应cut_for_search，且三者均可以通过参数HMM决定是否使用
新词识别功能。
=====================
1>cut_all=True, HMM=_对应于全模式，即所有在词典中出现的词都会被切分出来，实现函数
为__cut_all；
2>cut_all=False, HMM=False对应于精确模式且不使用HMM；按Unigram语法模型找出联合
概率最大的分词组合，实现函数为__cut_DAG；
3>cut_all=False, HMM=True对应于精确模式且使用HMM；在联合概率最大的分词组合的基
础上，HMM识别未登录词，实现函数为__cut_DAG_NO_HMM。
"""
import jieba


seg_list = jieba.cut("我来到北京清华大学", cut_all=True)  # 全模式
print("Full Mode:" + "/".join(seg_list))  # seg_list属于一个generator类型的对象

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)  # 精确模式
print("Default Mode:" + "/".join(seg_list))

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print("/".join(seg_list))  # 此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
# 搜索引擎模式
print("/".join(seg_list))
seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=True)
print("/".join(seg_list))  # 此为全模式，对比上面搜索引擎模式


