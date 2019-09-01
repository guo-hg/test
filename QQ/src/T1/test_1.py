#!/sur/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from time import  sleep
import yaml
import pytest
from until.ReadDate import  s
from until.mylog import get_logger
log = get_logger(filename="test_1.py")

with open(file=r'E:\QQ\element\login.yaml', mode='r', encoding='utf-8') as f:
    e = yaml.load(f, Loader=yaml.FullLoader)
    # print(e)


# d = {
#     "platformName": "Android",                            #系统型号
#     "platformVersion": "5.1.1",                           #系统版本
#     "deviceName": "emulator-5554",                        #系列号
#     "appPackage": "com.tencent.mobileqq",                 # 安装包名
#     "appActivity": ".activity.SplashActivity",            #活动栈
#     "noReset": "true",                                    #
#     "unicodeKeyboard": "true"
# }
# #  建立连接，并开启QQ程序
# dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
# #  等待程序启动
# sleep(10)
# #执行退出账号的操作


# def test_One(lian):
#         #lian = dr
#     lian.find_element_by_xpath(e['tou']).click()      #  头像的xpath
#     sleep(3)
#     lian.find_element_by_id(e['seting']).click()      #  点击设置
#     sleep(3)
#     lian.find_element_by_id(e['zhanghao']).click()    # 点击账号管理
#     sleep(3)
#     lian.find_element_by_id(e['tuihao']).click()      #点击退出当前账号
#     sleep(3)
#     lian.find_element_by_id(e['tuichu']).click()      #点击确定退出
#     sleep(3)
#     a = lian.find_element_by_accessibility_id(e['xinyonghu']).text
#     print(a)
#     assert  a == "用户注册"
    # 退出QQ程序
    # lian.quit()


def test_2(lian):
    # 先清除账号
    lian.find_element_by_accessibility_id(e['zhanghuming']).clear()
    sleep(2)
    # 在输入账号
    lian.find_element_by_accessibility_id(e['zhanghuming']).send_keys("452286292")
    sleep(2)
    # 在输入密码
    lian.find_element_by_id(e['password']).clear()
    sleep(2)
    lian.find_element_by_id(e['password']).send_keys("guo18991002302..")
    sleep(2)
    #  登录
    lian.find_element_by_id(e['denglu']).click()