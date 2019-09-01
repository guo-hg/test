#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from until.日志 import get_logger


log = get_logger(filename='test_1.py')


def test_1():
    dr = webdriver.Chrome()
    dr.get('https://mail.163.com/')
    dr.maximize_window()
    log.info("163邮箱连接成功，并且最大化")
    dr.find_element_by_id('switchAccountLogin').click()
    sleep(3)
    log.info("选择账号密码登录")
    dr.switch_to.frame(dr.find_element_by_xpath('//*[@scrolling="no" and @frameborder="0" ]'))
    log.info("切换框架成功")
    dr.find_element_by_name('email').send_keys("guohg18991002302")
    log.info("账号输入成功")
    dr.find_element_by_name('password').send_keys('guo18991002302..')
    log.info('密码输入成功')
    dr.find_element_by_id('dologin').click()
    sleep(3)
    log.info('登录成功')
    dr.find_element_by_id('_mail_component_24_24').click()  # 写信
    sleep(3)
    dr.find_element_by_class_name('nui-editableAddr-ipt').send_keys('13592386651')
    log.info("填写收件人成功")
    dr.find_element_by_xpath('//*[@class="nui-ipt-input" and @type="text" and @tabindex="1"]').send_keys('web自动化')
    sleep(3)
    log.info('主题填写成功')
    dr.switch_to.frame(dr.find_element_by_class_name('APP-editor-iframe'))
    dr.find_element_by_class_name('nui-scroll').send_keys('hello')
    sleep(3)
    dr.switch_to.parent_frame()  # 退回到上一层的框架
    dr.find_elements_by_class_name('nui-toolbar-item')[0].click()
    log.info('发送成功')
    dr.quit()



