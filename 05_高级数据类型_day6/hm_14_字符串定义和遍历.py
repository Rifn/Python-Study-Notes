str1 = "hello python"
str2 = '我的外号是"大西瓜"'

print(str2)
print(str1[6])

for char in str2:

    print(char)
str3 = "武汉是百湖之城"
print(str3[::1])
print(str3[1::1])
x1 = str3[len(str3)-1:]
print(x1)
x2 = str3[len(str3)-1::-1]
print(x2)
x3 = x2.lstrip("城").rstrip("武")
print(x3)
