#!/sur/bin/python
# -*-coding:utf-8-*-
#!/sur/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from time import sleep
import  yaml
import pytest
from until.滑动 import swipe_up
from until.滑动 import swipe_down
from selenium.common.exceptions import NoSuchElementException
from until.日志 import get_logger


log = get_logger(filename="test_4.py")

#  调用yaml文件元素
with open(file=r'E:\APP\element\appluogin.yaml', mode='r', encoding='utf-8') as f:
    e = yaml.load(f, Loader=yaml.FullLoader)
    # print(e)

def test_1(lian):
    log.info("成功连接APP")
    lian.find_element_by_id(e['dianji']).click()   #  点击密码按钮
    sleep(5)
    lian.find_element_by_id(e['zhanghao']).click()  # 点击输入账号
    sleep(2)
    lian.find_element_by_id(e['zhanghao']).send_keys("13319264301")  # 输入账号
    log.info("账号输入成功")
    sleep(3)
    lian.find_element_by_id(e["mima"]).click()                  # 点击输入密码
    sleep(3)
    lian.find_element_by_id(e["mima"]).send_keys("g123456")    # 输入密码
    log.info("密码输入正确")
    sleep(3)
    lian.find_element_by_id(e["denglu"]).click()         #  点击登录按钮
    sleep(5)
    a = lian.find_element_by_id(e["zhibo"]).text                 # 登录成功之后的界面
    log.info("成功登录")
    assert  a ==  "直播"
    sleep(5)
def test_2(lian):
    lian.find_element_by_id("android:id/tabs").find_elements_by_id("com.qk.butterfly:id/v_main_tab")[-1].click()
    a1 = lian.find_element_by_id(e["bianji"]).text
    log.info("跳转成功")
    assert a1 == "编辑资料"
    sleep(3)
#测试三：点击编辑资料，进入编辑页面
def test_3(lian):
    lian.find_element_by_id(e["ziliao"]).click()
    a2 = lian.find_element_by_id(e["bian"]).text
    assert a2 == "编辑资料"
    log.info("成功进入编辑资料页面")
    lian.find_elements_by_class_name("android.widget.ImageView")[-1].click()
    sleep(3)
    lian.find_element_by_id("com.qk.butterfly:id/btn_album").click()
    sleep(3)
    lian.find_element_by_id("com.qk.butterfly:id/iv_1").click()
    sleep(3)
    lian.find_elements_by_class_name("android.widget.ImageView")[-1].click()
    sleep(3)
    lian.find_element_by_id("com.qk.butterfly:id/btn_album").click()
    sleep(3)
    lian.find_element_by_id("com.qk.butterfly:id/iv_1").click()
    sleep(3)
    lian.find_element_by_id("com.qk.butterfly:id/tv_top_right").click()
    sleep(10)
    log.info("添加照片成功")
    a4 = lian.find_element_by_id("com.qk.butterfly:id/tv_top_right").text
    assert a4 == "编辑资料"
    log.info("成功跳转")
def test_4(lian):
    swipe_up(lian)
    sleep(2)
    log.info("滑动成功")
def test_5(lian):
    lian.find_element_by_id(e["shezhi"]).click()
    sleep(3)
    a5 = lian.find_element_by_id(e["ok"]).text
    assert a5 == "退出登录"
    log.info("点击设置跳转界面成功")
    sleep(4)
# 测试十：退出登录
def test_6(lian):
    lian.find_element_by_id(e["ok"]).click()
    sleep(5)
    a6 = lian.find_element_by_id(e["ok1"]).text
    assert a6 == "确定"
    sleep(3)
    lian.find_element_by_id(e["ok1"]).click()
    log.info("退出成功")




