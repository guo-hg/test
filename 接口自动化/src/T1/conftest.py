#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest



@pytest.fixture(scope="module")
def jk():
    url = "http://v.juhe.cn/cccn/to_telecodes.php"
    return  url