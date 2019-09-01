#!/sur/bin/python
# -*-coding:utf-8-*-
from  appium import webdriver


def swipe_left(driver,t=500):               #  往左滑
#  第一步：  获取手机屏幕的大小
    a = driver.get_window_size()
#  第二步： 放缩屏幕
    x1 = a["width"] * 0.2
    x2 = a["width"] * 0.9
    y1 = a["height"] * 0.25
    y2 = a["height"] * 0.5
    driver.swipe(x2,y1,x1,y1,t)
def swipe_right(driver,t=500):                # 往右滑
#  第一步：  获取手机屏幕的大小
    a = driver.get_window_size()
    x1 = a["width"] * 0.5
    x2 = a["width"] * 0.75
    y1 = a["height"] * 0.25
    y2 = a["height"] * 0.5
    driver.swipe(x1,y1,x2,y1,t)
def swipe_up(driver,t=500):                # 往上滑
#  第一步：  获取手机屏幕的大小
    a = driver.get_window_size()
    x1 = a["width"] * 0.5
    x2 = a["width"] * 0.75
    y1 = a["height"] * 0.1
    y2 = a["height"] * 0.9
    driver.swipe(x1,y2,x1,y1,duration=t)
def swipe_down(driver,t=500):                # 往下滑
#  第一步：  获取手机屏幕的大小
    a = driver.get_window_size()
    x1 = a["width"] * 0.5
    x2 = a["width"] * 0.75
    y1 = a["height"] * 0.1
    y2 = a["height"] * 0.9
    driver.swipe(x1,y1,x1,y2,duration=t)