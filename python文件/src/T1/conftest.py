#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
@pytest.fixture()
def clean():
    print("当账号密码输错的时候，执行删除数据的操作")