#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
from appium import webdriver
from time import  sleep
import yaml

# QQ项目

@pytest.fixture(scope="module")
def lian():
    d = {
        "platformName": "Android",                            #系统型号
        "platformVersion": "5.1.1",                           #系统版本
        "deviceName": "emulator-5554",                        #系列号
        "appPackage": "com.tencent.mobileqq",                 # 安装包名
        "appActivity": ".activity.SplashActivity",            #活动栈
        "noReset": "true",                                    #
        "unicodeKeyboard": "true"
    }
#  建立连接，并开启QQ程序
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#  等待程序启动
    sleep(10)
    dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()
    sleep(2)
    return dr




