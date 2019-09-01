#!/sur/bin/python
# -*-coding:utf-8-*-
# 定义一个函数，参数x为必填参数，参数y为可变长参数
# # 求函数传入x的值+传入y的值的和
def a(x,*args):
    a = x
    for i in args:
        # print(type(i))
        a += i
    # print(a)
    return  a
print(a(100,1,2,1,1))

