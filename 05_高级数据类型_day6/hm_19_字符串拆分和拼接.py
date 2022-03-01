# 假设：以下内容是从网络上抓取的
# 要求：
# 1. 将字符串中的空白字符全部去掉
# 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"

print(poem_str)

# 1. 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 2. 合并字符串
result = " ".join(poem_list)
print(result)

# 3> strip() 函数
str_s = " aaccbb11abc11bac "
str_s1 = str_s.strip()  # 不加参数时，默认去掉空格
print(str_s1, len(str_s1))
str_s2 = str_s.strip("aa")
print(str_s2)  # 将参数分解为不同元素，去掉原字符串中首尾两端
# 所有包含这些元素的值

str_s.lstrip()  # 分别从左右去掉某些字符
str_s.rstrip()

