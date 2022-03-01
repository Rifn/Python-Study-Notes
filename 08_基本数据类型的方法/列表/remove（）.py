
list1 = [1, 2, 3, 4]

list2 = []
for i in list1:
    if i == 1:
        del list1[list1.index(i)]
    else:
        num = i + 1
        list2.append(num)

print(list1)
print(list2)
