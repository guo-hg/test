#!/sur/bin/python
# -*-coding:utf-8-*-
from  appium import webdriver
from time import sleep


# 实现自动化登录QQ，发消息，到退出QQ

d = {
    "device": "android",                        # 设备类型 android
    "platformName": "Android",                  # 设备的名字
    "platformVersion": "8.0.0",                 # 安卓系统版本
    "deviceName": "SQRNW17805006828",           # 手机序列号
    "appPackage": "com.tencent.mobileqq",       # app的包名
    "appActivity": ".activity.SplashActivity",  # app的活动名
    "noReset": "true",                          # 该参数为保存用户操作数据
    "unicodeKeyboard":"true"                    # 启用appium键盘

}

dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d)     #  与手机建立连接
dr.find_element_by_id("com.tencent.mobileqq:id/login").click()                   #  点击登录QQ
s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")  #循环点击菜单键
for i in s:
    i.click()
    sleep(3)
dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").click()  #  点击消息菜单键
dr.find_element_by_id("com.tencent.mobileqq:id/recent_chat_list").find_element_by_class_name("android.widget.LinearLayout").click()
dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys("小比")    #  发消息
dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()              # 点击发送
n = dr.find_element_by_id("com.tencent.mobileqq:id/rlCommenTitle").find_elements_by_id("com.tencent.mobileqq:id/name")
n[5].click()       #  返回

dr.find_element_by_id("com.tencent.mobileqq:id/conversation_head").click()   # 点击图像
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()         #  点击设置
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()   #  点击账号管理
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()        # 点击退出当前账号
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()    #  点击确定