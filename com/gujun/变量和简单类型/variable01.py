# 变量
# python是弱类型语言：
#   1.变量无须声明即可赋值，对一个不存在的变量赋值相当于定义一个新变量；
#   2.变量的数据类型可以动态改变；(和JavaScript一样)
a=22
print(type(a))  #<class 'int'>
a='gujun'
print(type(a))  #<class 'str'>

#使用print()输出变量
#print()可以输出多个变量，默认以空格作为分隔符，可以通过sep参数来设置
#默认情况下，print()输出完都会换行，是因为end参数默认值为'\n'
print('name','gujun',sep=':')   #name:gujun
#file参数指定print()输出目标,默认为sys.stdout，即标准输出（控制台屏幕），可以修改该参数让其输出到指定文件
f=open('out.txt','w');
print('hello gujun',file=f);
f.close();
# flush参数控制输出缓存，一般设为false即可；

