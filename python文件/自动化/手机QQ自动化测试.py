#!/sur/bin/python
# -*-coding:utf-8-*-

from appium import  webdriver
from time import sleep

# python代码客户端连接手机客户端所需要的信息

d = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": ".activity.SplashActivity",
    "noReset": "true",
    "unicodeKeyboard":"true"
    }


#  步骤一：与手机建立连接

dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d) #  地址不变 http://localhost:4723/wd/hub
# dr.find_element_by_id("com.tencent.mobileqq:id/login").click()                   #  点击登录QQ
"""
将手机信息发送到appium服务器，使服务器和手机建立一个session（会话）
appium与python客户端建立一个连接
"""
sleep(5)

"""
id: 一般是唯一的，标记一个元素
class：标记一组元素，一般是多个
test：判断是否可以获取文字，有文字代表可以获取
clickable：判断是否可以被点击，true可以被点击，false不可以被点击
"""
#  第二步： 执行操作
"""
id不唯一，使用class进行定位
解决方法：
    向上一级、或者向上上一级查找ID唯一，class唯一
    在使用class进行定位
"""

# 先找唯一的ID，在找class
#  联系人，看点，动态  三个组成的列表
s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
for i in s:
    i.click()
    sleep(3)
  # 消息的可点击的定位
dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").click()
#  点击搜索
# dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").click()
# dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys("李伟")
# q = dr.find_element_by_class_name("android.widget.RelativeLayout").click()
# q[1].click()
 # 找出消息栏中的文字
d = dr.find_element_by_id("android:id/tabs").find_elements_by_id("com.tencent.mobileqq:id/name")
for i in d:
    print(i.text)
    sleep(3)

# m = dr.find_element_by_id("com.tencent.mobileqq:id/recent_chat_list").find_element_by_class_name("android.widget.LinearLayout").click()
# dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys("龟儿子")    #  发消息
# dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()              # 点击发送
# n = dr.find_element_by_id("com.tencent.mobileqq:id/rlCommenTitle").find_elements_by_id("com.tencent.mobileqq:id/name")
# n[3].click()       #  返回

# dr.find_element_by_id("com.tencent.mobileqq:id/conversation_head").click()   # 点击图像
# sleep(3)
# dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()         #  点击设置
# sleep(3)
# dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()   #  点击账号管理
# sleep(3)
# dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()        # 点击退出当前账号
# sleep(3)
# dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()    #  点击确定





#  点击动态看朋友圈
s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")  #  点击动态
s[-1].click()
sleep(3)
dr.find_element_by_id("com.tencent.mobileqq:id/qzone_feed_entry").click()
sleep(5)

