#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
d = [1,2,3,4,5,6,7]
@pytest.fixture(scope='function',params=d)
def  read_data(request):                         #  request   必须写成这样，固定写法， 作用取出参数列表中每一个元素，
    print(f"当前的传入参数值是{request.param}")   #  request.param:作用：与request结合使用，取出参数
    return request.param

def test_1(read_data):
    t = read_data          #  t 是一个实际结果
    # 预期结果  6
    assert   t < 6
# 传入两个参数

# d2 = [(1,2),[2,2],[3,4]]
#
#
# @pytest.mark.parametrize("y1,y2",d2)
# def test_2(y1,y2):
#     print(f"y1的值是{y1}")
#     print(f"y2的值是{y2}")
#     assert y1 == y2





# @pytest.fixture(autouse="true")
# def myfix():
#     print("每个测试用例要跑mysfix")
# def test_3():
#     pass
# def test_4():
#     pass


# def myfix():
#     print("每个测试用例要跑mysfix")
# pytestmark=pytest.mark.usefixtures("myfix")
# def test_1():
#     pass
# def test_2():
#     pass

# @pytest.fixture()
# def myfix():
#     print("每个测试用例要跑mysfix")
#
# @pytest.mark.usefixtures('myfix')
# def test_1():
#     print("用例1开始执行")
#
# @pytest.mark.usefixtures('myfix')
# def test_2():
#     print("用例2开始执行")