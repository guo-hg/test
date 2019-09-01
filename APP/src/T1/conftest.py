#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
from appium import webdriver
from time import sleep
import yaml


#  这个py文件存放一些共用的函数，

#  连接碟声(模拟机)
@pytest.fixture(scope="module")
def lian():
    d = {
        "platformName": "Android",                # 系统型号
        "platformVersion": "5.1.1",               # 系统版本
        "deviceName": "emulator-5554",            # 系列号
        "appPackage": "com.qk.butterfly",         # 安装包名
        "appActivity": ".main.LauncherActivity",  # 活动栈
        "noReset": "true",  #
        "unicodeKeyboard": "true"
    }
#  建立连接，并开启碟声程序
    dr = webdriver.Remote(r"http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#  等待程序启动
    sleep(10)
    return dr


