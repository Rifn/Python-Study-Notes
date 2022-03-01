def fill(your_list):
    # 将序列中的股票代码补全为六位的方法
    list1 = []
    for i in your_list:
        if len(i) == 6:
            num1 = i
            list1.append(num1)
        else:
            num2 = ("0"*(6-len(i))) + i
            list1.append(num2)
    return list1


def add(your_list):
    list1 = []
    for i in your_list:
        num = "x" + i
        list1.append(num)
    return list1


def remove_first(your_list):
    list1 = []
    for i in your_list:
        num = i[1] + i[2] + i[3] + i[4] + i[5] + i[6]
        list1.append(num)
    return list1


def catch6(your_list):
    list1 = []
    for i in your_list:
        num = i[2] + i[3] + i[4] + i[5] + i[6] + i[7]
        list1.append(num)
    return list1

