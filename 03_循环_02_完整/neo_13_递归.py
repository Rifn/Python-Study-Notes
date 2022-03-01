import sys


def test(n):  # 该递归函数是一个死循环，没有 break 条件，但python中的最大递归深度为997
    print(n)
    n += 1
    test(n)


# sys.setrecursionlimit(3000)  # 可以修改最大递归深度
# test(1)

def age(n):  # 18 20 22 24
    if n == 1:
        return 18  # 可直接 return 18
    else:
        a = age(n - 1) + 2
        return a  # 可直接return age(n-1) + 2


print(age(4))

# # 三级菜单查询
# dic = {
#     "河南": {
#         "郑州": {
#             "二七纪念塔": {},
#             "河南省博物院": {},
#             "龙湖": {}
#         },
#         "洛阳": {
#             "龙门石窟": {},
#             "明堂": {},
#             "老君山": {}
#         }
#     },
#     "湖北": {
#         "武汉": {
#             "东湖": {},
#             "黄鹤楼": {},
#             "木兰草原": {}
#         },
#         "宜昌": {
#             "三峡大坝": {},
#             "清江画廊": {}
#         },
#     },
#     "安徽": {
#         "合肥": {
#             "中科大": {},
#             "巢湖": {}
#         },
#         "黄山": {
#             "黄山景区": {},
#             "古徽州": {},
#             "牯牛降": {}
#         },
#     }
# }
#
#
# def threeLM(your_dic):
#     while True:
#         for k in your_dic: print(k)
#         key = input(">>>").strip()
#         if key == "b" or key == "q": return key
#         elif key in your_dic.keys() and your_dic[key]:
#             ret = threeLM(your_dic[key])
#             if ret == "q":
#                 return "q"
#
#
# threeLM(dic)
# print(dic["河南"])


# 二分查找算法
list1 = [2, 3, 5, 7, 18, 19, 20, 55, 58, 66, 67, 81, 83, 89, 90, 91]
print(list1.index(66))
i = 0
for num in list1:
    if num == 66:
        print(i)
    i += 1


# def func(your_list, aim):
#     mid = (len(your_list) - 1) // 2
#     if your_list:
#         if aim > your_list[mid]:
#             func(your_list[mid+1], aim)
#         elif aim < your_list[mid]:
#             func(your_list[:mid], aim)
#         elif aim == your_list[mid]:
#             print("找到了", mid)
#     else:
#         print("找不到")
#
#
# func(list1, 66)

# # 升级版二分法
# def search_num(num, l, start=None, end=None):
#     start = start if start else 0
#     end = end if end is not None else len(l) - 1
#     mid = (end - start) // 2 + start
#     if start > end:
#         return None
#     elif l[mid] > num:
#         return search_num(num, l, start, mid-1)
#     elif l[mid] < num:
#         return search_num(num, l, mid+1, end)
#     elif l[mid] == num:
#         return mid
#
#
# print(search_num(58, list1))


