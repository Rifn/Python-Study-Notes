import jieba


TestStr = "2018年底部队友谊篮球赛结束"
# 因为在汉语中没有空格进行词语的分隔，所以经常会出现中文歧义，比如：
# 年底-底部-部队-队友。jieba默认启用了HMM(隐马尔可夫模型)进行中文分词，实际效果不错

seg_list = jieba.cut(TestStr, cut_all=True)  # 全模式
print("Full Mode:" + "/".join(seg_list))

seg_list = jieba.cut(TestStr, cut_all=False)  # 默认模式
print("Default Mode:" + "/".join(seg_list))  # 默认模式下有对中文歧义较好的分类方式

seg_list = jieba.cut_for_search(TestStr)  # s搜索引擎模式
print("Cut for Search:" + "/".join(seg_list))
