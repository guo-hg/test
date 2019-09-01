#!/sur/bin/python
# -*-coding:utf-8-*-


# python 与系统交互
# 系统包括：  windows，max，  unix
# python的内置模块   ——>  python 自带的，下载时包含的
# os库


import os

#第一个   获取当前目录 ——>  类似于  linux - pwd
#  使用方法   os.getcwd()
# a = os.getcwd()
# print(a)

#第二个  切换到指定目录，  os.chdir(目录名字)
# os.chdir("A")
# b = os.getcwd()
# print(b)

#  第二个  返回当前目录  os.curdir     代表字符串 "."
os.chdir(os.curdir)
c = os.getcwd()
#print(c)

#  第三个  返回上一级目录  os.pardir
os.chdir(os.pardir)
d = os.getcwd()
#print(d)


#  获取操作系统类型     os.name
#   "nt"  是  windows   'posix'
# n = os.name
# print(n)

#  创建多级目录   A/a/b
#os.makedirs("AAA/BBB/CCC")

#   创建一个目录
#os.mkdir("DDD")

#  删除多个目录     删除的是空目录   不是空不能删除
#os.remove("B")

#  删除单个目录   只删除空目录
#os.rmdir("DDD")

#  查看当前路径下所有的文件，目录，包含隐藏 类似 ： ls -al
# x = os.listdir(r"E:\untitled1\python\AA")
# print(x)

#  对文件，目录进行重命名
# os.rename(r"E:\untitled1\python\AA",r"E:\untitled1\python\AAA")

#  删除文件
#os.remove(r"E:\untitled1\python\B\2.xls")

# 执行系统命令
# a = os.popen("dir")
# print(a.read())

# 目录树
# for root , dirs, files in os.walk(r"E:\untitled1\python"):
#     print(files)


#  os.path类  对文件的操作
# 1   返回文件的绝对路径
#      abspath(文件名)
a = os.path.abspath("A")
# print(a)

# 2   返回文件的上一级目录名
#b = os.path.dirname(r"E:\untitled1\python\A")
# print(b)

# 3.  返回当前文件的目录
#c = os.path.basename(r"E:\untitled1\python\2.xls")
# print(c)

#  4.  判断文件是否存在  -->  返回布尔值
#d = os.path.exists(r"E:\untitled1\python\2.xls")
# print(d)

# 5  判断是否为目录
# x = os.path.isdir(r"E:\untitled1\python\2.xls")
# y = os.path.isdir("B")
# print(x)
# print(y)

#  6  判断是否为文件
# q = os.path.isfile("2.xls")
# print(q)

# 7 .判断是否为链接文件
# w = os.path.islink("2.xls")
# print(w)

#  8 . 文件路径拼接
# e = os.path.join('\python','asdf')
# print(e)

# 9.文件路径分离   将前一个文件/目录  和最后一个进行分割，返回一个元组
#r = os.path.split(r"E:\untitled1\python\2.xls")
#print(r)

# 10  分割文件后缀名  返回一个元组
#t = os.path.splitext(r"E:\untitled1\python\2.xls")
#print(t)


#  题目  统计当前目录下有多少个文件，目录
# a = os.getcwd()                           #获取当前目录
# print(a)
# b = os.listdir(r"E:\untitled1\python")   #查看当前路径下所有的文件，目录，包含隐藏
# print(b)
# m = 0
# n = 0
# for i in range(len(b)):
#     x =os.path.isdir(b[i])           #  判断是否为目录
#     y =os.path.isfile(b[i])        #   判断是否为文件
#     if x == True:
#         m += 1
#     if y == True:
#         n += 1
# print(m)
# print(n)

#   第二种方法

# class Wen(object):
#     def a(self):
#         a1 = os.listdir(r"E:\untitled1\python")
#         a2 = 0
#         a3 = 0
#         for i  in  a1:
#             if os.path.isdir(i):
#                 a2 = a2 +1
#             if os.path.isfile(i):
#                 a3 = a3 +1
#         return f"当前目录下有{a2}个目录，{a3}个文件"
#     # print(a2)
# ss = Wen()
# print(ss.a())






import  time
# #python 对时间的操作
#
#
# #    1、睡眠     sleep（数）      浮点数、整数     单位是秒    休眠的是cpu的线程
# print("睡眠之前")
# time.sleep(0.5)
# print("睡眠之后")
#
# #   2、cpu运行代码的时间
# print(time.clock())
#
# #   3、 本地时间
# print(time.ctime())
# print(time.asctime())
#
# #   4 、输出时间的详细信息
# print(time.localtime())
#

# #  5 、格式化输出时间
# print(time.strftime("%A %d %B %H:%S"))
# print(type(time.strftime("%A %d %B %H:%S")))
#
#
# #  6、  根据格式解析表示时间的字符串
# print(time.strptime("30 Nov 00", "%d %b %y"))
#
#
# #  7、 距离计算机元年过去多少秒   1970.1.1
# print(time.time())




#  python对日期的操作
from  datetime import datetime,date,timedelta
#  1.获取当前时间、日期
print(datetime.now())


#  2、  获取指定的时间日期
# print(datetime(1989,2,28,12,1,1))


# 3、字符串转日期
# t = datetime.strptime('1989-02-28 12:01:01','%Y-%m-%d %H:%M:%S')
# print(t)

# 4 、 日期转字符串
# s = datetime.now().strftime("%A %d %B %H:%S")
# print(s)

#  5 日期的加减法
# now = datetime.now()
q = datetime.now() - timedelta(days= 5)
print(q)
#
# # 6、获取当前日期
print(date.today())
#
# #  7 、 对日期的加减
f = date.today() - timedelta(days= 2)
print(f)