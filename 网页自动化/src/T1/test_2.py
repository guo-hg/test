#!/sur/bin/python
# -*-coding:utf-8-*-

from selenium import webdriver
from time import sleep
from until.日志 import get_logger

log = get_logger(filename='test_2.py')


def test_1(qingka):
    dd = qingka.current_window_handle
    print(dd)
    qingka.find_element_by_link_text('主播入口').click()
    log.info("进入主播入口")
    dd = qingka.window_handles
    print(dd)
    qingka.switch_to.window(dd[-1])
    print(qingka.title)
    a = qingka.title
    assert a == '情咖电台'
    log.info("切换窗口成功")
def test_2(qingka):
    qingka.find_element_by_id('userName').click()
    qingka.find_element_by_id("userName").send_keys("13319264301")
    qingka.find_element_by_id('password').click()
    qingka.find_element_by_id('password').send_keys("g123456")
    qingka.find_element_by_id('submitLogin').click()
    log.info("登陆成功")


