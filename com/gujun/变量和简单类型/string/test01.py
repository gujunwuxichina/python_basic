# 字符串可以包含任何字符，包括中文；可以用单引号或双引号包含；
# 对于字符串中出现的某些字符要进行转义；
# 若将两个字符串紧挨在一起，python会自动拼接它们：
s1='gujun' 'wuxi'
print(s1)   #gujunwuxi
# 用+拼接也行；
# python不允许直接拼接数值和字符串，必须先将数值转换为字符串；可以使用str()或repr()；
n1=100
print(s1+str(n1))
print(s1+repr(n1))
# str()和repr()都可以将数值转为字符串，str是Python内置的类型，repr()是函数，repr还有一个功能，会以python表达式的形式来表示值：
print(s1)
print(repr(s1)) # 输出的内容带有引号的字符串，即python的表达式内容；
# input()，生成一条提示信息，然后获取用户的输入，将输入内容放入字符串并返回，无论输入那种内容都会转为字符串；
s2=input("你的输入:")
print(s2)
print(type(s2)) #str
# 长字符串，即用三个单/双引号包含的字符串，如果长字符串没有赋值给任何变量，则相当于该字符串被解释器忽略了即注释；
# 由于python不是自由格式的语言，对于换行、缩进有其规定，表达式不允许随便换行，若需要换行可以使用转义字符对换行符进行转义；
n2=3+\
    4
print(n2) #7