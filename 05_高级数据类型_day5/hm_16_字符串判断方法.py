# 1. 判断空白字符
space_str = "      \t\n\r"

print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# 1> 都不能判断小数
# num_str = "1.1"
# 2> unicode 字符串
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

"""
而python内置的库，已经帮你实现了这个功能了。最最最致命的是，我之前已经用过这个方法了，
但是在实际使用的时候，我没有用上。我大可以说，这个是粗心，就和考试的时候一样，问什么数
字平方等于4，我只写了个2，然后因此丢了-2那半分，但我知道，这其实就是基础不夯实的体现。
是一种凭借直接经验获取知识的思维方式。毕竟python字符串判断方法，在日常开发中，用的比较少，
因此被我忽视掉了。为了避免以后再犯类似的错误，就趁此机会捡起烂笔头。总结一下该知识点，防止
以后再忘记

1.startswith | 判断是否以某字符串开头
实例：

2.endswith | 判断是否以某字符串结尾
示例：

3.isupper | 判断是否至少存在一个大写字母，且所有字母均大写
示例：

4.islower | 判断是否至少存在一个小写字母，且所有字母均小写
示例：

5.isdigit | 判断是否全部为非负整数
示例：

6.isalpha | 判断是否全部为字母
示例：

7.isalnum | 判断是否全部为非负整数或字母（即 isdigit or isalpha）
示例：

8.isspace | 判断是否全为空格（包含制表符）
示例：

9.istitle | 判断是否为首字母大写（忽略非字母字符）
示例：

10.isdecimal | 判断是否全为阿拉伯数字非负整数（只接受unicode形式输入）
示例：

11.isnumeric | 判断是否全为非负整数（只接受unicode形式输入）
示例：

以上就是python2中的字符判断函数集合，python3中引入了三个新的字符判断函数，让字符判断功能更
加强大

12.isidentifier | 判断是否为python内部关键字或有效标志符
示例：

13.isprintable | 判断是否可打印（包括空字符串）
示例：

14.isascii() | 判断是否为ascii码【American Standard Code for Information Interchange 
(美国信息交换标准码)】
"""