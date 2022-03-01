"""
str.split(sep=None, maxsplit=-1)
==================================
Return a list of the words in the string, using sep as the delimiter string.
If maxsplit is given, at most maxsplit splits are done (thus, the list will
have at most maxsplit+1 elements). If maxsplit is not specified or -1, then
there is no limit on the number of splits (all possible splits are made).
If sep is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings (for example, '1,,2'.split(',') returns
['1', '', '2']). The sep argument may consist of multiple characters
(for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an
 empty string with a specified separator returns [''].
"""

# 要将文本文件中的隔行分割开来，需要用分隔符(定界符)【\n】
str0 = "今天\n中午\n我\n吃了\n牛肉面"
print(str0)
str1 = str0.split("\n")
print(str1)

print('1,2,3'.split(','))
print('1,2,3'.split(',', maxsplit=1))
print('1,2,,3,'.split(','))

"""
If sep is not specified or is None, a different splitting algorithm is applied:
runs of consecutive whitespace are regarded as a single separator, and the 
result will contain no empty strings at the start or end if the string has
leading or trailing whitespace. Consequently, splitting an empty string or a 
string consisting of just whitespace with a None separator returns [].
For example:
"""

print('1 2 3'.split())
print('1 2 3'.split(maxsplit=1))
print(' 1 2 3 '.split())
