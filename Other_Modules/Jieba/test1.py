import jieba

text = "今天中午我吃了榨菜肉丝面"
seg_list = jieba.cut(text, cut_all=False)
text1 = "/".join(seg_list)
print(text1)
text2 = text1.split("/")
print(text2)

menu_text = "牛肉面\n关东煮\n肉丝面"
menu_list = menu_text.split("\n")
print(menu_list)

# 比较出两个文本中相同的词语
for mylaunch in text2:  # 第一种方法
    for food in menu_list:
        if mylaunch == food:
            print(mylaunch)

for mylaunch in text2:  # 第二种方法
    if mylaunch in menu_list:
        print(mylaunch)
