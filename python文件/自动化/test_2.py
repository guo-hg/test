#!/sur/bin/python
# -*-coding:utf-8-*-
from appium import  webdriver
from time import sleep


def test_1():
    d = {
        "platformName": "Android",                   #设备类型
        "platformVersion": "5.1.1",                  #安卓版本
        "deviceName": "emulator-5554",               #序列号
        "appPackage": "com.qk.butterfly",            #安装包名
        "appActivity": ".main.LauncherActivity",     #活动名
        "noReset": "true",                           #保护用户操作数据
        "unicodeKeyboard":"true"                     #启用键盘
        }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d)  #  与模拟机进行连接
    sleep(3)
    dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()              #  点击密码登录
    sleep(3)
    dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").click()  #点击输入账号框
    sleep(2)
    dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").send_keys("13319264301")  #  输入账号
    dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").click()        #点击输入账号
    sleep(3)
    dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").send_keys("g123456")
    sleep(2)
    dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").click()         #点击登录
    sleep(3)
    b = dr.find_element_by_id("android:id/tabhost").find_element_by_class_name("android.widget.RelativeLayout").click()
    # .find_element_by_class_name("android.widget.RelativeLayout")
    # b[-1].click()



