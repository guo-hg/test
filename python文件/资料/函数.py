#!/sur/bin/python
# -*-coding:utf-8-*-


#   python   函数
#函数的作用
"""
1.使代码重复被使用
2.减少代码量

#定义： 一段代码的封装被称为函数
"""

"""
书写格式： 
1.定义函数的关键字    def
2.函数名：要符合变量的命名规则
3.参  数：必填参数，默认参数，可变长参数
4.返回值：使用关键字   return            return会将结果返回给函数名，然后直接打印这个函数名
"""
#    b 是要返回的结果

"""
#定义函数
def  a(x):
    #写求和代码
    b = 0
    for i in range(x):
        b += i
    print(b)           # 没有返回的结果
    return b            #返回None
    #return            # 要是return都不写，也返回None
a(101)
print(a(101))
"""

# 1.一个函数使用return，但是没有返回的结果的时候，返回None【空值】
# 2.一个函数不适用return的时候，返回None【空值】




#使用函数

# 1.函数的名字
# 2.有参数对参数进行赋值





#a = "全局变量"

#定义之后整个脚本都可以用

#print(a)


#  局部变量       定义之后只能在一定的范围内使用


# def m():
#     n = "局部变量"
#     return  n
#
# m()       #  等价于 “局部变量”
#
# print(m())


#global()   1.将局部转变为全局变量     2.修改全局变量的数据类型

#第一种  将局部转变为全局变量
# def m():
#     global p    # 代表全局变量
#     p = 100      # 局部变量
#     return p
# print(m())
# #   验证p是否是全局变量
# print(p)

#第二种  修改全局变量的数据类型       当全局变量和局部变量是同一个变量名的时候，函数优先使用局部变量
#                                   当函数内没有局部变量时，向上查找相同名字的全局变量
#                                     找不到需要的全局变量时，代码报错，
# g =   "全部变量"   # str
# print(type(g))
# def k():
#     global g            # 全局变量
#     g = 100
#     #g = "局部变量"
# k()
# print(g)
# print(type(g))




#pycharm   调试

#红点：  被称为调试断点，进入调试模式:使用绿色的小虫子

# def k(x1,x2):
#     c = x1 + x2
#     print(c)
#     return  c
# k(100,200)



#函数的作用域

#从定义函数的那一行开始一直到return那一行结束




#函数 ：阶乘之和
# def jiecheng(x):
#     a = 1
#     b = 0
#     for i in range(1,x+1):
#         a = a * i
#         b = b + a
#     print(b)
#     return b
# jiecheng(5)
# print(jiecheng(5))


# 函数的参数分类
# 1.必填参数，参数定义之后，在函数 被使用的时候，必须传入，赋值的参数

# def k(x1,x2):
#     c = x1 + x2
#     print(c)
#     return  c
#
# k(100,200)


#2.默认参数：在参数被定义的时候，参数有一个默认值，在函数使用的时候，
#   对默认参数赋值，则使用赋予的值，不对默认参数赋值，就使用默认值
"""
def k(x1,x2=5000):
    # x2 = 5000     x2 默认参数，    默认值是5000
    c = x1 + x2
    print(c)
    return  c

k(100,)    #使用默认参数
k(100,200)  #不使用默认参数
"""


#3.  可变长参数    #第一种：   以元组的形式赋值
# def  canshu(*args):
#     x1,x2,x3 = args
#     print(args)
#     print(x1)
#     print(x2)
#     print(x3)
# canshu(1,2,3)

#以元组的形式赋值    例子
# def d(*cc):
#     e=len(cc)
#     for i in range(0,e):
#         a=f"s_{i}"
#         print(f"参数值是{a}，对应值是{cc[i]}")
# d(1,2,3,"q","w","e")

# 定义方法取出字典中的值
# def get_val(_dict):
#     val = list(_dict.values())[1]  # 根据值进行排序：将.values()改为.keys()就ok了
#     print(val)
#     return val
# get_val({1:[213],2:[234]})

#   第二种       以字典形式赋值
#
# def k(**gh):       #kwargs   字典，关于字典的所有函数都可以适用
#     print(gh)

# #参数传递   写法一
# k(a = 1,b = 2,c = 3 )
# print(type(k))

# #写法二     先写成一个字字典，  用**传递    **变量名
#
# n = { "x1": 1 ,"x2":2, "x3":3}
# k(**n)




#函数的嵌套


#第一种

# def f():
#     # 语句体
#     return "我是f的第一个函数"
# def k():
#     print("此时运行函数k")
#     print(f())    #执行f函数
# k()



#第二种

# def foo():
#     x = 100   #  局部变量
#     def k():
#         c = x * 10
#         return c
#     return  k()          # 可以在k后面加（）
# print(foo())            #也可以在foo（）后面加



#匿名函数
# 1、函数没有名字
# 2、使用lamdba定义
# 3、使用和函数的作用相同


"""
lambda 参数1,参数2,:函数的输出语句块
"""

# import  random    #   生成随机数
# a = lambda  n : random.randint(1,10) * n
# print(a(2))


# b = [i for i in range(1,10)]
# print(b)
# b.reverse()      #   reverse    反转
# print(b)
# print(b[:: -1])

"""
python 列表推导式
定义：
1.生成的结果是新的列表
2.使用循环语句，if语句
3，使用python的库【模块】
4,函数

书写格式：
[ 表达式  循环语句  判断语句 ]
"""
# a = [ i for i in range(1,11) if i > 5]
# print(a)

# l = [lambda n : n + 1  for i in range(1,11) if i > 5]
# print(l[4](10))
#
#
#
# b =[[1,2],[3,4],[5,6]]
# a = [x for y in b for x in y  ]
# print(a)





# a = input("输入字符串")
# print(type(a))
# b = a[:: -1]
# c = 0
# for i,j in enumerate(b):
#     for n in range(9):
#         if str(n) == j:
#              d = j *(10**i)
#     c = d + c
# print(a)
# print(type(a))