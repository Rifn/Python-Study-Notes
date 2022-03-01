import jieba

text = "今天中午我吃了榨菜肉丝面"
seg_list = jieba.cut(text, cut_all=False)
text1 = "/".join(seg_list)
print(text1)
text2 = text1.split("/")
print(text2)

menu_text = "牛肉面/关东煮/肉丝面"
menu_list = menu_text.split("/")
print(menu_list)

myword_list = []
for myword in text2:
    if not(myword.strip() in menu_list) and len(myword.strip()) > 1:
        myword_list.append(myword)
print(myword_list)
