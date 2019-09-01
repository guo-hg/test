#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
from appium import  webdriver
from time import sleep
import yaml
from selenium.common.exceptions import NoAlertPresentException
from until.日志 import get_logger

log = get_logger("test_5.py")

# 调用yaml文件里的元素
with open(r"E:\APP\element\appluogin.yaml") as  f:
    e = yaml.load(f,Loader=yaml.FullLoader)


def test_1(lian):
    log.info("成功连接APP")
    lian.find_element_by_id(e['dianji']).click()   #  点击密码按钮
    sleep(5)
    lian.find_element_by_id(e['zhanghao']).click()  # 点击输入账号
    sleep(2)
    lian.find_element_by_id(e['zhanghao']).send_keys("13319264301")  # 输入账号
    log.info("账号输入成功")
    sleep(3)
    lian.find_element_by_id(e["mima"]).click()                  # 点击输入密码
    sleep(3)
    lian.find_element_by_id(e["mima"]).send_keys("g123456")    # 输入密码
    log.info("密码输入正确")
    sleep(3)
    lian.find_element_by_id(e["denglu"]).click()         #  点击登录按钮
    sleep(5)
    a = lian.find_element_by_id(e["zhibo"]).text                 # 登录成功之后的界面
    log.info("成功登录")
    assert  a ==  "直播"
    sleep(5)