# 整型
# python3的整型支持各种整数值，不像其他变成语言有short、int、long;
a=100;
print(a)
print(type(a))  # <class 'int'>
a=22**22
print(a)
print(type(a))  # <class 'int'>,python2也许会显示<class 'long'>即把大整数当成long类型；
b=None  #python整型支持None即空值
print(b)    # None
# 整型数的4种表示形式
# 1.十进制；2.二进制,0b或0B开头；3.八进制,0o或0O开头；4.十六进制,0x或0X开头;
# 为了提高可读性，Python3允许为数值增加下划线作为分隔符
c=1_000_000
print(c)