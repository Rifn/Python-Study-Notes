
# 列表推导式提供了一种简练的创建列表法方法
list1 = [x for x in range(0, 6)]
print(list1)

list2 = [x*x for x in range(0, 6)]  # 各语句之间是嵌套关系，左边的第二个语句是最外层，
# 依次往左进一层，最左边是最后一层
print(list2)

# 还可以这么做
list3 = [3, 5, 8]
list4 = [x for x in range(0, 10) if x not in list3]
print(list4)
# 以上代码等价于
list5 = []
for x in range(0, 10):
    if x not in list3:
        list5.append(x)
print(list5)
# 这极大地简化了代码
