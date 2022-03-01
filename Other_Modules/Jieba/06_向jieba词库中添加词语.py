"""
jieba.add_word(new_word)
==========================
向jieba词库中添加新的词语
"""
import jieba


text = "水杯龙王"
seg_list = jieba.cut(text, cut_all=True)
print("/".join(seg_list))

new_word = "杯龙"
jieba.add_word(new_word)
seg_list = jieba.cut(text, cut_all=True)
print("/".join(seg_list))
