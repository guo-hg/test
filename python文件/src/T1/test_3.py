#!/sur/bin/python
# -*-coding:utf-8-*-
#  测试用例初始化环境问题


"""

清理测试环境的机制

第一步：在用例执行之前进行环境清理
第二步：在用例执行之后进行环境清理

"""

#  第一种：脚本级别的清理
#  setup_module     用例执行之前的
#  teardown_module  用例执行之后的
#  module  本脚所有用例执行前，后的操作仅执行一次

import  pytest
# def setup_module():
#     print("所有用例执行之前执行一次")
# def test_1():
#     print("用例一执行")
# def test_2():
#     print("用例二执行")
# def test_3():
#     print("用例三执行")
# def teardown_module():
#     print("所有用例执行之后执行一次")

#pytest -s  输出测试用例中print内的信息                    #    pytest -s   test_3.py

#  setup_function   每个测试用例运行之前都要执行一次
#  teardown_function  每个测试用例运行之后都要执行一次

# def setup_function():
#     print("每个用例执行之前执行一次")
#
# def test_1():
#     print("用例一执行")
# def test_2():
#     print("用例二执行")
# def test_3():
#     print("用例三执行")
# def teardown_function():
#     print("每个用例执行之后执行一次")


# setup,  teardown   在类的范围内使用
# class  TestOne(object):
#     def setup(self):
#         print("执行setup")
#     def teardown(self):
#         print("执行teardown")
#     def test_4(self):
#         print("执行测试用例4")
#     def test_5(self):
#         print("执行测试用例5")
#     def test_6(self):
#         print("执行测试用例6")


#  setup  -->   每个测试用例执行之前运行一次
#  teardown --> 每个测试用例执行之后运行一次


# setup_class    --> 代表类中的所有用例执行之前运行一次
# teardown_class  -->代表类中的所有用例执行之后执行一次

# class  TestOne(object):
#     def setup_class(self):
#         print("执行setup_class")
#     def teardown_class(self):
#         print("执行teardown_class")
#     def test_4(self):
#         print("执行测试用例4")
#     def test_5(self):
#         print("执行测试用例5")
#     def test_6(self):
#         print("执行测试用例6")

#setup_method       -->   每个测试用例执行之前运行一次   方法级别
# teardown_method   -->   每个测试用例执行之后运行一次


# class  TestOne(object):
#     def setup_method(self):
#         print("执行setup_method")
#     def teardown_method(self):
#         print("执行teardown_method")
#     def test_4(self):
#         print("执行测试用例4")
#     def test_5(self):
#         print("执行测试用例5")
#     def test_6(self):
#         print("执行测试用例6")


#  测试夹具    fixture
# @pytest.fixture()
'''
scope:装饰器的作用范围
    funtion  方法级别，默认             #  在指定的用例之前，清理环境
    class    类级别                     #  每次执行类里面所有的测试用例之前，只清理一次测试环境
    module   脚本级别
    package  目录级别
    session  会话级别，多个测试用例组合的时候使用
'''

#  第一种级别：方法级别
# @pytest.fixture()
# def login():
#     print("login函数开始执行")
#
# def test_1(login):
#     print("执行用例1")
# def test_2(login):
#     print("执行用例2")
# def test_3():
#     print("执行用例3")


#  第二种级别：  类级别
# class TestThree(object):
#     @pytest.fixture(scope="class")
#     def login_1(self):
#         print("执行login_1方法")
#
#     def test_4(self,login_1):
#         print("执行用例4")
#
#     def test_5(self,login_1):
#         print("执行用例5")
#     def test_6(self,login_1):
#         print("执行用例6")


"""
module:  脚本级别，在测试用例执行之前运行一次，仅只运行一次，使用方式：在测试用例的（放被@pytest.）

"""

# @pytest.fixture(scope="module")
# def start():
#     print("所有的测试用例之前运行一次")
# @pytest.fixture(scope="module")
# def close():
#     print("用例之前运行一次，只运行一次")
#
# def test_1(start):
#     print("执行用例一")
# def test_2(start):
#     print("执行用例二")
# def test_3(close):
#     print("执行用例三")


"""
conftest.py   作用：python脚本文件，用来存放公共函数,被不同的测试用例使用
test脚本下     一般只写以test开头的函数，类，方法
注意事项：conftest.py 必须放在当前测试用例所有的目录下面
src/T1/test_1.py   那conftest.py文件必须放在T1目录下面

"""
# @pytest.fixture()
# def clean():
#     print("当账号密码输错的时候，执行删除数据的操作")
# def test_1(clean):
#     print("输入账号，密码")
#
# def test_2(clean):
#     print("输入账号，密码")
#
# def test_3(clean):
#     print("输入账号，密码")





#  参数化   向测试用例中传入参数的过程

# d = [1,2,3,4,5,6,7]
# @pytest.fixture(scope='function',params=d)
# def  read_data(request):                         #  request   必须写成这样，固定写法， 作用取出参数列表中每一个元素，
#     print(f"当前的传入参数值是{request.param}")   #  request.param:作用：与request结合使用，取出参数
#     return request.param
#
# def test_1(read_data):
#     t = read_data          #  t 是一个实际结果
#     # 预期结果  6
#     assert   t < 6



# 传入两个参数

# d2 = [(1,2),[2,2],[3,4]]
#
#
# @pytest.mark.parametrize("y1,y2",d2)
# def test_2(y1,y2):
#     print(f"y1的值是{y1}")
#     print(f"y2的值是{y2}")
#     assert y1 == y2









# @pytest.fixture()
# def myfix():
#     print("每个测试用例要跑myfix")
#
# @pytest.mark.usefixtures('myfix')
# def test_1():
#     pass
#
# @pytest.mark.usefixtures('myfix')
# def test_2():
#     pass



# def myfix():
#     print("每个测试用例要跑mysfix")
# pytestmark=pytest.mark.usefixtures("myfix")
# def test_1():
#     pass
# def test_2():
#     pass
#
#
#
@pytest.fixture(autouse="true")
def myfix():
    print("每个测试用例要跑mysfix")
def test_3():
    pass
def test_4():
    pass





#  pytest  支持跳过某些用例，失败重跑，统计测试覆盖率等