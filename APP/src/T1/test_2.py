#!/sur/bin/python
# -*-coding:utf-8-*-
from time import  sleep
import yaml
import pytest
from selenium.common.exceptions import NoSuchElementException
from until.日志 import get_logger
from until.用户名密码组合 import s

log = get_logger(filename="test_2.py")


with open(file=r"E:\APP\element\appluogin.yaml",mode="r",encoding="utf-8") as f:
     e = yaml.load(f,Loader=yaml.FullLoader)
with open(file=r"E:\APP\data\a.txt",mode="r",encoding="utf-8") as fb:
    datas = fb.read().split(";")


@pytest.mark.parametrize("zh,mm",s)
def test_1(zh,mm,lian):
    log.info("连接成功")
    # 点击密码按钮
    # lian.find_element_by_id(e["dianji"]).click()
    # 先清除账号
    lian.find_element_by_id(e['zhanghao']).clear()
    sleep(2)
    # 在输入账号
    log.info(f"账号{zh}")
    lian.find_element_by_id(e['zhanghao']).send_keys(zh)
    sleep(2)
    # 在输入密码
    log.info(f"密码{mm}")
    lian.find_element_by_id(e['mima']).clear()
    sleep(2)
    lian.find_element_by_id(e['mima']).send_keys(mm)
    sleep(2)
    #  登录
    lian.find_element_by_id(e['denglu']).click()
    sleep(3)
    log.info("登录成功")