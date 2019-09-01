#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest


def test_1():
    a = 1
    b = 2
    c = a + b
    # 实际结果是3，预期结果是2
    # 设定断言
    assert c == 2


def test_2():
    str_1 = "hello pytest"
    str_2 = "python"
    # 设定断言，判断str_2 在 str_1内
    assert str_2 in str_1


def test_three():
    n = 100
    # 设定断言，判断n小于101
    assert n < 10