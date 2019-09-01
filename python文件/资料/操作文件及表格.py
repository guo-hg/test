#!/sur/bin/python
# -*-coding:utf-8-*-

#open(): 打开文件，txt文件，Excel
#如何查看代码
# 1.选中
# 2.Ctrl+ b

#open()

"""
常用参数
1.file：     文件的名字，a.txt   b.excel
2.mode='r'     读取文件的模式    r——读取模式    w——写入模式     a——追加写入模式
                              b——二进制写入   + 追加  读写
3。encoding=None      指定文件的编码方式       utf - 8     gbk
"""


#写入过程
# f = open("b.txt",mode="w",encoding="utf-8")
# # write()       写入   传入字符串   想写入的文字
# f.write("hello,python \nsdfsafsdfs")
# #  close()   关闭
# f.close()


#读取文件
# f = open("a.txt",mode="r",encoding="utf-8")
# #   read()   读取文件中所有内容
# text=f.read()
# print(text)
# f.close()

# #例子 ；写入
# a = ["a","b","c"]
# f = open("a.txt",mode="w",encoding="utf-8")
# for i in a:
#     f.write(i+"\n")
# f.write(f"{i}\n")
# f.write("a\n""b\n""c\n")
# f.close()


# f = open("b.txt",mode="r",encoding="utf-8")
#readlines(n)      每次读取一行， n有数值，只读取数值的行数
# text= f.readlines(1)         #  返回一个列表
# c =[]
# for j in text:
#     c.append(j.strip())
# print(c)
# f.close()
# print(text)
#
#
# def wj(x):
#     f = open(file=x, mode="r", encoding="utf-8")
#     print(f.readlines(2))
#     b = []
#     for i in f:
#         b.append(i.strip())
#     f.close()
#     return f
# wj("a.txt")












#            python读取Excel表格中的数据，需要使用的第三方包(pip install excel)
import xlrd

#   打开Excle文件
# d = xlrd.open_workbook(filename="12.xls")
#   获取Excel表格，返回的是一个包含所有excel的表格
#   假设文件中存在两个excel表，那么列表中【‘sheetl’‘sheet2’】
# table = d.sheets()[0]
# #  获取表中的数据       row_values()   获取整行的数据，必须指定获取的行号
# x = table.row_values(1,0)         #     行从0开始,后一个是从那一列开始
# y = table.row_values(0,1)
#print(x)
# print(y)
# #
# #     获取某个单元格的值     先通过row获取某一行，返回列表，在通过列表索引获取元素，通过【.value】获取到具体的值
# dan = table.row(0)[1].value
#print(dan)
# # #    获取某一列的值，  先通过col获取某一列，返回列表，在通过列表索引获取元素，通过【.value】获取到具体的值
# lie = table.col(1)[1].value
#print(lie)
# # #    获取某一行的某一列的值
# huoqu = table.cell(0,1).value
# print(huoqu)
# # #   获取行数
# hang = table.nrows
#print(hang)
# # #   获取列数
#lieshu = table.ncols
# print(lieshu)
# # #  通过行数获取所有的数据
# for i in range(hang):
#     print(table.row_values(i))
# #
# # #  通过列数获取所有的数据
# b = table.col_values(1)      #  获取整列的数据
# print(b)

#for j in range(lieshu):
    #print(table.col_values(j))
#
# #打印/输出 excel表得名字    d 代表打开excel文件
#print(d.sheet_names())      #找出文件中所有表的名字
#
#
# #  通过索引获取表
# # 假设一个文件存在两个表sheet1，sheet2，  sheet_by_index():   0  打开的就是sheet1
# table = d.sheet_by_index(0)
# print(table)




#  打开某个表格，并将所有的内容保存到txt文档中
# class Excel(object):
#     def __init__(self,name,num):
#         self.d = xlrd.open_workbook(filename=name)    #   打开文件
#         #  使用某一张表
#         self.t = self.d.sheets()[num]        #d.sheet_by_index(0)    两种方法#shuju = dui.data()#shuju =#shuju = dui.data() dui.data()
#     #  data 方法的作用，获取一张表中的所有的数据
#     def a(self):
#         #  将所有数据装到一个列表中
#         biao = []
#         n = self.t.nrows      # 获取行数
#         for i in range(n):
#             #print(self.t.row_values(i))
#             biao.append(self.t.row_values(i))
#         return biao
# class Txt(Excel):
#     def write_data(self):
#         f = open(file="wen.txt",mode="w",encoding="utf-8")
#         shuju = self.a()             #shuju = dui.data()
#         for i in shuju:
#             print(i)
#             for j in i:
#                 #print(j)
#                 f.write(f"{str(j)} " '\t')
#             f.write("\n")
# t1 = Txt("12.xls",0)
# t1.write_data()



# 向excel文件中写入数据     xlwt      pip  install  xlwt
# import  xlwt
# #  新建一个excel文件
# d = xlwt.Workbook()
# # 新建一个excel表            add_sheet("工作表的名字")    必填
# table = d.add_sheet("表1")
# #  写入数据到excel表中
# #  一次写入一个单元格    第一个0是行，第二个0是列
# table.write(0,0,"张三")
# table.write(0,12,"李四")
# # 保存文件              save("文件名")    必填
# d.save("7,3.xls")


# import xlwt
#
# a = [["序号","名字","年龄","性别"],["1","王二","12","男"],["2","张三","23","女"],["3","李四","12","男"],
#      ["4" ,"赵六","32","女"]]
# d = xlwt.Workbook()
# table = d.add_sheet("表1")
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         table.write(i,j,a[i][j])
# d.save("例子.xls")


import  xlwt
# class A(object):
#     c = xlwt.Workbook()    #新建excel文件
#     def __init__(self,biao,shuju):
#         self.table = self.c.add_sheet("表")  # 新建表
#         self.biao = biao
#         self.shuju = shuju
#     def b(self):
#         for i in range(len(self.shuju)):
#             for j in range(len(self.shuju[i])):
#                 self.table.write(i,j,self.shuju[i][j])
#         self.c.save(self.biao)                            #  保存文件
#
# q = A("2.xls",[['序号', '名字', '年龄', '性别'], [1.0, '张三', 20.0, '男'], [2.0, '李四', 19.0, '男'], [3.0, '王五', 18.0, '女'], [4.0, '赵信', 16.0, '女']])
# q.b()









#导入 （跨文件夹）
#      from 文件夹名字  import  脚本名

#同文档导入
#  第一种
#from  a import 脚本名        #导入全部   from a  import  *
#  第二种
#from  文件路径 import  *     #  文件路径=  python.A.aa      eg:   from python.A.aa import *   print(a)  print(b)


#将九九乘法表写入到txt文件
class A(object):
    def __init__(self,x):
        self.x = x
        self.f = open("c.txt",mode="w",encoding="utf-8")
    def b(self):
        for i in range(1,self.x):
            for j in range(1,i+1):
                self.f.write(f"{j}*{i}={i*j} \t")
            self.f.write("\n")
a = A(10)
a.b()




"""
#将九九乘法表写入到Excel文件
import xlwt
class A(object):
    def __init__(self,x):
        self.x = x
         #  新建一个excel文件
        self.d = xlwt.Workbook()
        # 新建一个excel表               必填
        self.table = self.d.add_sheet("表1")
    def jiu(self):
        for i in range(1,self.x):
            for j in range(1,i+1):
                self.table.write(i-1,j-1,f"{j}*{i}={i*j}")
        # # 保存文件              save("文件名")    必填
        self.d.save("99.xls")

a = A(10)
a.jiu()
"""

import  xlwt
# class A(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.a = self.x + self.y
# class B(A):
#     def b(self):
#         print(self.a)
# c =B(1,2)
# c.b()


# class A(object):
#     def __init__(self,x):
#         self.x = x
#         self.d=xlwt.Workbook()
#         self.table = self.d.add_sheet("99")
#     def b(self):
#         for i in range(1,self.x):
#             for j in range(1,i+1):
#                 self.table.write(i-1,j-1,f"{j}*{i}={i*j}")
#         self.d.save("99.xls")
# a = A(10)
# a.b()