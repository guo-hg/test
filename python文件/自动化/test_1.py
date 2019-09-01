#!/sur/bin/python
# -*-coding:utf-8-*-

"""
pytest,是python自动化测试一个工具库
作用：
    1、调整测试用例的运行顺序
    2、对测试用例传入测试数据
    3、对测试用例设置断言
    4、pytest与allure生成测试报告
特点：
    灵活，支持的插件丰富
"""
import pytest

#自动化测试用例指的是？
#    指的是一个函数，这个函数必须以test开头。
def test_0():
    #计算100以内的和
    a = 0
    for i in range(101):
        a = a + i
    #  预期结果是5050，
    #  实际结果是a
    #断言指的是：拿实际结果与预期结果进行对比的过程
    assert a == 5051
#执行测试用例有两个命令：
#    1、pytest -v   模块名
#    2、py.test  -v 模块名            AssertionError   断言错误
# 运行测试用例，生成测试报告：
# 第一步：py.test test_1/ --alluredir ./result/            #运行用例，保存到result目录下
# 第二步、allure generate ./result/ -o ./report/ --clean   #生成测试报告，并保存到report目录下
# 第三步、allure open -h 127.0.0.1 -p 8083 ./report/       #打开测试报告


""" 
pytest  
查找当前目录下，所有文件或目录，找包含test目录和文件
如果找到以test开头的目录，类似于cd进去，开始执行搜索包含test开头的文件，在接着搜索以test开头所有的函数
整个当前目录下没有包含test开头的文件和目录，就会报错：_____ERROR collecting test session ____



pytest -v  输出的信息会更加详细                          #    pytest  -v
pytest -q  简化输出信息                                  #    pytest  -q
pytest -s  输出测试用例中print内的信息                    #    pytest -s   test_3.py
pytest -k  执行包含设定“关键字”的用例                     #    pytest -k "test_three"
pytest     脚本名::用例名字   -->   执行脚本中的具体用例   #    pytest test_1.py::test_2

"""

