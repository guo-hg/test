#!/sur/bin/python
# -*-coding:utf-8-*-


#pip  python的第三方包下载工具，下载python的第三方包
# 什么是python的包
# python脚本文件的汇总集合被称为包
#pip命令
# pip  install   包名     下载
# pip  list   查找pip下载过的所有包
import pymysql
# #第一步：连接数据库
# connect = pymysql.connect(
#     host="192.168.10.32",      #   数据库所在的主机IP地址/域名 【运服务器——mysql数据库】
#     port=3306,                 #  mysql的端口号
#     user="root",               # mysql的用户名
#     password="123456",         #  mysql的用户密码
#     charset="utf8",            # mysql数据的编码方式
#     #database="库名"           #指定数据库，不写这个参数，默认使用所有的数据库
# )
# cu = connect.cursor()        #     第二步   游标  类似于mysql >  命令行模式
# sql = "create database su19"      #第三步   建库 ，保存数据到数据库
# #执行sql语句                      第四部    关闭
# cu.execute(sql)
#输出查询结果（一张表只能有一种查询结果）
# fetchall()  查所有    fetchone()  查一条       fetchmany(size=4)
# b =cu.fetchall()
# print(b)
# #保存数据到数据库
# self.connect.commit()
# #关闭
# def close(self):
#     #与数据库断开连接
#     self.connect.close()



class Mysql(object):
    connect = pymysql.connect(
        host="192.168.0.152",
        port=3306,
        user="root",
        password="123456",
        charset="utf8",
        )
    cur =connect.cursor()    #  创建游标
#  创建库
    def create_databases(self):
        # 写 sql语句
        sq = "create database d3 default charset utf8 collate utf8_general_ci"
        # 执行sql
        self.cur.execute(sq)
#  创建表
    def create_table(self):      #  普通方法
        sq = "use d3"
        sq0= "create table a3 (number char(10))"
        self.cur.execute(sq)
        self.cur.execute(sq0)
# # 添加数据
    def insert_table(self):
        cur = self.connect.cursor()
        q = "use d3"
        w = "insert into a3 values ('郭')"
        self.cur.execute(q)
        self.cur.execute(w)
a = Mysql()
# a.create_databases()
a.create_table()
a.insert_table()





class A(object):
    def __init__(self):                                     #  连接数据库
        self.a=pymysql.connect(
            host = "192.168.10.14",
            port = 3306,
            user = "root",
            password ="123456",
            charset = "utf8",
            database = "python"
        )
        self.a1 = self.a.cursor()                        #  创建游标
    def c(self):
        sq2 = "create table p1 ( number int(10))"          #  建表
        self.a1.execute(sq2)
    def d(self):
        sq4 = "insert into p1 values (1)"
        self.a1.execute(sq4)
k = A()
k.c()
k.d()





