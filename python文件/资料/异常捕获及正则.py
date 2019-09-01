#!/sur/bin/python
# -*-coding:utf-8-*-



#     python 异常处理
#1、错误          一，python语法错误，包括书写格式，缩进
#                 二，代码逻辑，python解释器无法编译解释，导致python报错
# 2、异常         处理错误的过程被称为异常处理


#   3 、try   ...   except   最简单的异常处理
"""

try:
    d = 1/0
    print(d)
except OverflowError:
    print("异常已经被处理")
except  ZeroDivisionError:
    print("异常被处理")
"""



#     4、try   ...   except ...finally       finally最终都会被执行它下面的代码
"""
try:
    d = 1/0
    print(d)
except OverflowError:
    print("OverflowError异常已经被处理")
except  ZeroDivisionError:
    print("ZeroDivisionError异常被处理")
finally:
    print("无论异常是否被处理，都会输出finally下面的代码")
"""


#    5、try   ...except... else


# try:
#     d = 1/10
#     print(d)
# except OverflowError:
#     print("OverflowError异常已经被处理")
# except  ZeroDivisionError:
#     print("ZeroDivisionError异常被处理")
# else:
#     print("不存在异常，执行else下面的代码")






#  python with
#  with   应用场合：  只要是操作系统资源，建立连接，python线程，进程的关闭释放
#   with 一种概念：   上下文管理
#   用于对文件的操作
# with open(打开文件的操作)   as   变量名  ：
#           代码
# 最后就会自动关闭这个程序


# with  open(file="a.txt",mode="w",encoding="utf - 8")  as   f:
#     a = f.write("你好，阿彪")
# print(a)


#     python正则      只能匹配字符串
#  正则模块  re

import   re


s = "abcabgsagsag"
#  编译正则表达式
#   .   代表除了\n  以外的所有字符，一个. 代表一个字符
# x = re.compile('...')                #  这个过程就是编译
#
# #  匹配正则  match (编译过的正则表达式，字符串)    匹配不成功返回None
# res = re.match(x,s)
# print(res)
#
# a = re.match('...',s)
# print(a)

#  * 代表匹配*前面的字符0次或者多次
# x = re.compile('abc*')
# res = re.match(x,s)
# print(res)

#  +  匹配+号前面的字符一次或者多次
# x = re.compile('abc+')
# res = re.match(x,s)
# print(res)

#  ？ 匹配？前面的字符0次或者一次
# x = re.compile('abc?')
# res = re.match(x,s)
# print(res)



#s = "abbabgsagsab"
# ^  匹配字符串以某个字符开头
# x = re.compile('^ab')
# res = re.match(x,s)
# print(res)

#  $  匹配字符串以某个字符结尾
# x = re.compile('ab$')
# res = re.match(x,s)
# print(res)

#  {m} 匹配{}前面的字符出现的指定次数
# x = re.compile('ab{1}')
# res = re.match(x,s)
# print(res)

#s = "abbbbbbbabgsagsab"
#  {m,n}   匹配{}前面的字符出现的指定次数,    最少m次，最多n次  尽可能匹配n次
# x = re.compile('ab{1,44}')
# res = re.match(x,s)
# print(res)

#  []   匹配【】内的任意一个字符，只匹配一次。
# x = re.compile('a[a-z]')
# res = re.match(x,s)
# print(res)


#s = "abbbbbbbabgsagsab"
#  |  或   匹配|左右的表达式
# x = re.compile('ab|c]')
# res = re.match(x,s)
# print(res)


#  \D   匹配不是十进制的字符     \d  匹配任何十进制数字的字符
#    \s  匹配空白字符    包括（  空格，\t,\n,\f,\v）   \S   匹配非空白字符

#   ()   匹配括号内的字符     group()   获取匹配到的内容


# print(res)
# print(res.group())

#re.search(正则表达式，要匹配的字符串)     从左向右对整个字符串进行搜索匹配，匹配不到返回None，匹配到第一个就停止匹配

#b = re.compile('w')

#  re.findall(正则表达式，要匹配的字符串)   从左向右对整个字符串进行搜索匹配，
#                                       匹配到的内容放到列表中，如果使用（）值匹配（）里的内容  出来的结果以列表的形式显示


#贪婪模式   .*    尽可能匹配多的字符          非贪婪模式  .*?     匹配到字符就停止
# j = "http://www.baidu.comhttp://www.360.com"
# b = re.compile('http://www.(.*).com')
# res = re.match(b,j)
# a = re.findall(b,j)
# print(a)
#
# j = "http://www.baidu.comhttp://www.360.com"
# b = re.compile('http://www.(.*?).com')
# res = re.match(b,j)
# a = re.findall(b,j)
# print(a)


#re.sub( 正则表达式，要替换的字符串，要匹配的字符)
g = "hello world"
k = re.sub("l","kk",g)
print(k)



#   re.S   给点 加功能   让 点  匹配包括换行符在内的任意字符     re.I  不区分大小写
#把f使用正则-->  g

