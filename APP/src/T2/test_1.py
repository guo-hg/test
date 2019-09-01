#!/sur/bin/python
# -*-coding:utf-8-*-
import allure
import pytest

#  feature : 作用是标注测试用例是属于哪个模块
@allure.feature("模块一")
def test_1():
    assert 0 == 0


@allure.feature("模块一")
def test_2():
    assert 0 < 1



# story: 对一个测试用例的详细描述

@allure.feature("模块二")
@allure.story("这是一个很棒的测试用例")
def test_3():
    assert  0 > 123213

@allure.feature("模块二")
@allure.story("这是一个很垃圾的测试用例")
def test_4():
    """
    这是对函数参数，返回值的一个讲解
    感觉很nice
    """
    #测试用例的描述是通过函数的注释来获取到的

    assert  "香港屌丝很多" in "china"


# 测试用例的优先级
"""
Blocker级别:  阻塞  中断缺陷
Critical级别：严重缺陷
Normal级别：  普通缺陷
Minor级别：   次要缺陷（界面错误与UI需求不符）
Trivial级别： 轻微缺陷（必输项无提示，或者提示不规范）
"""


#  severity  标注测试用例的优先级


@allure.feature("模块三")
@allure.severity("blocker")
def test_5():

    assert  0 == 1


@allure.feature("模块三")
@allure.severity("critica")
def test_6():
    assert 0 == 0

@allure.feature("模块三")
@allure.severity("normal")
def test_7():
    assert 3 == 3

@allure.feature("模块三")
@allure.severity("minor")
def test_8():
    assert 3 == 5


@allure.feature("模块三")
@allure.severity("trivial")
def test_9():
    assert 3 == 4


# step 记录测试用例中的一些步骤  日志代码可以通过step记录到报告中

@allure.step("字符串相加:{0},{1}")
#isinstance(参数一，参数二)，判断数据类型的类，参数一和参数二是否是同一个类型
#  是的话，返回 Ture
#  不是的话，返回 False
def str_add(str1, str2):
    if not isinstance(str1, str):
        return f"{str1}不是字符串类型的"
    if not isinstance(str2, str):
        return f"{str2}不是字符串类型的"
    return str1 + str2


@allure.feature("模块四")
def test_11():
    str1 = "hello"
    str2 = "world"

    assert  str_add(str1,str2)   == "helloworld"

# Issue和TestCase定制详解
#  对issue和testcase生成网址
def str_12(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('模块五')
@allure.issue("http://www.baidu.com")             #   放测试用例的bug存在问题
@allure.testcase("http://www.testlink.com")        #  放测试用例的详细内容
def test_13():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'