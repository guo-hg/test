#!/sur/bin/python
# -*-coding:utf-8-*-
from appium import webdriver



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
    y1 = a["height"] * 0.25
    y2 = a["height"] * 0.5
    driver.swipe(x1,y2,x1,y1,duration=t)
def swipe_down(driver,t=500):                # 往下滑
#  第一步：  获取手机屏幕的大小
    a = driver.get_window_size()
    x1 = a["width"] * 0.5
    x2 = a["width"] * 0.75
    y1 = a["height"] * 0.25
    y2 = a["height"] * 0.5
    driver.swipe(x1,y1,x1,y2,duration=t)
#  往右滑
# dr.swipe(x1,y1,x2,y1,t = 500)


# 往上滑
# dr.swipe(y2,x1,y1,x1)








# swipe(self, start_x, start_y, end_x, end_y, duration=None)
#     Swipe from one point to another point, for an optional duration.
#     从一个点滑动到另外一个点，duration是持续时间
#
#     :Args:
#     - start_x - 开始滑动的x坐标
#     - start_y - 开始滑动的y坐标
#     - end_x - 结束点x坐标
#     - end_y - 结束点y坐标
#     - duration - 持续时间，单位毫秒
#
#     :Usage:
#     driver.swipe(100, 100, 100, 400)
