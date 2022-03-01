"""
str.strip( [ chars ] )
=======================
Return a copy of the string with the leading and trailing characters removed.
The chars argument is a string specifying the set of characters to be removed.
If omitted or None, the chars argument defaults to removing whitespace.
The chars argument is not a prefix or suffix; rather, all combinations of its
values are stripped:
"""

str0 = "   spacious   "
print(str0)
str1 = str0.strip()
print(str1)

str2 = "www.example.com"
print(str2)
print(str2.strip("cmow."))
print(str2.strip("owm.c"))
