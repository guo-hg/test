#!/sur/bin/python
# -*-coding:utf-8-*-


"""
appium 的三种等待
1、sleep  -->   强制等待  工作的线程会停止一段时间
"""
#第二种等待   隐性等待   -->  mplicitly_wait(10)  :意思就是在10秒钟等待某个元素出现，在10秒内没出现，会抛出异常
#  设置最大等待时间，关键字参数：time_to_wait=10，超过最大等待时间后则会抛出异常

# 第三种：安卓独有等待    wait_activity():
# 等待某个activity出现，设置最大等待时间，超出最大等待时间，就会抛出时间
# self.dr.wait_activity(activity=".activity.SplashActivity'', timeout=10)
#  只能用于等待activity

# 第四种  智能等待

#  WebDriverWait：等待某个元素加载出来
#  expected_conditions  的异常处理类
#  by  指的是通过什么方式进行定位  例如  By.ID    通过ID的方式定位的

from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait             #  WebDriverWait：等待某个元素加载出来
from selenium.webdriver.support import  expected_conditions  as  EC   #  expected_conditions  预期条件
from selenium.webdriver.common.by import By

WebDriverWait("参数一","参数二","参数三").until(EC.presence_of_all_elements_located("参数四"))

"""
参数一：我们与手机建立的会话   -->  dr
参数二：最大等待时间，单位是秒
参数三：刷新页面的时间间隔，单位是秒

until(EC.presence_of_all_elements_located("参数四"))
直到某个元素被找到，停止等待
参数四：一个定位方法，和元素组成的元组  eg: (By.ID,"元素")
"""
