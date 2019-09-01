#!/sur/bin/python
# -*-coding:utf-8-*-

import logging
import datetime



#  LOG_DIR  指日志文件夹/目录;日志文件格式为：日期.txt
LOG_DIR = "E:\\接口自动化\\log"



#  创建一个日志文件名字
a = LOG_DIR + str(datetime.datetime.now().date()) + ".txt"
# print(a)


# logging    是python定义一个日志的库
#定义日志输出的格式
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')

# print(formatter)
# logging的两种输出方式

# 第一种  输出到python控制台
c = logging.StreamHandler()      #  将日志输出到控制台
#  第二步：添加日志的样式
c.setFormatter(formatter)


#第二种  输出到文本里
w = logging.FileHandler(a,encoding="utf-8")
#  添加日志的样式
w.setFormatter(formatter)


def get_logger(filename):
    #  获取执行日志的脚本名字
    l = logging.getLogger("filename")
    # 添加输出内容到控制台
    l.addHandler(c)
    #  添加输出内容到文本
    l.addHandler(w)
    #  定义日志等级  致命，严重，轻微，建议————   INFO-最低级别-DEBUG  CRITICAL-致命的
    l.setLevel(logging.INFO)
    return l




