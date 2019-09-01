#!/sur/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from time import  sleep
import yaml
import pytest
from selenium.common.exceptions import NoSuchElementException
from until.mylog import get_logger
from until.ReadDate import s


log = get_logger(filename="test_10.py")       #  产生日志文件的脚本名


with open(file=r'E:\QQ\element\login.yaml', mode='r', encoding='utf-8') as f:
    e = yaml.load(f, Loader=yaml.FullLoader)
with open(file=r"E:\QQ\data\login.txt",mode="r",encoding="utf-8") as fb:
    datas = fb.read().split(";")
    # print(datas)



@pytest.mark.parametrize("y1,y2",s)
def test_2(y1,y2,lian):
    # 先清除账号
    lian.find_element_by_accessibility_id(e['zhanghuming']).clear()
    sleep(2)
    # 在输入账号
    log.info(f"账号{y1}")
    lian.find_element_by_accessibility_id(e['zhanghuming']).send_keys(y1)
    sleep(2)
    # 在输入密码
    log.info(f"密码{y2}")
    lian.find_element_by_id(e['password']).clear()
    sleep(2)
    lian.find_element_by_id(e['password']).send_keys(y2)
    sleep(2)
    #  登录
    lian.find_element_by_id(e['denglu']).click()
    sleep(15)

    try:
        a1 = lian.find_element_by_xpath(e['wangji']).text
        assert  a1 == "忘记密码"
        log.info(f"登录失败，断言成功{a1}")
    except NoSuchElementException:
        a2 = lian.find_element_by_id(e["queding"]).text
        assert  a2 == "确定"
        lian.find_element_by_id(e["queding"]).click()


    try:
        a3 = lian.find_element_by_id(e["xiaoxi"]).text
        assert a3 == "消息"
        log.info(f"登录成功，断言成功{a3}")
    except:
        pass





