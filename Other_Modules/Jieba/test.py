import jieba


text = "今天中午我吃了榨菜肉丝面"
seg_list = jieba.cut(text, cut_all=False)
print("/".join(seg_list))

menu_text = "牛肉面\n关东煮\n肉丝面"
print(menu_text)

menu_list = menu_text.split("\n")
print(menu_list)

text2 = "/".join(seg_list)
print(text2)
