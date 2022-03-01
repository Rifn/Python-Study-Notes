import jieba
import random


def jieba_processing_text(text):
    # jieba.add_word("朱亚男")
    jieba.add_word("把酒问青天")
    jieba.add_word("好的")
    jieba.add_word("化云化烟")
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/".join(seg_list)

    stop_word = ["只不过", "这个", "时而", "只有", "人才"]

    for myword in liststr.split("/"):
        if len(myword) > 1 and myword not in stop_word:
            num = random.randint(4, 13)
            for i in range(2, num):
                mywordlist.append(myword)
    return " ".join(mywordlist)
