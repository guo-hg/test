#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get('https://mail.163.com/')
dr.maximize_window()
dr.find_element_by_id('switchAccountLogin').click()
sleep(3)

dr.switch_to.frame(dr.find_element_by_xpath('//*[@scrolling="no" and @frameborder="0" ]'))
dr.find_element_by_name('email').send_keys("guohg18991002302")
dr.find_element_by_name('password').send_keys('guo18991002302..')
dr.find_element_by_id('dologin').click()
sleep(3)
dr.find_element_by_id('_mail_component_24_24').click()    #  写信
sleep(3)
dr.find_element_by_class_name('nui-editableAddr-ipt').send_keys('13592386651')
dr.find_element_by_xpath('//*[@class="nui-ipt-input" and @type="text" and @tabindex="1"]').send_keys('web自动化')
sleep(3)

dr.switch_to.frame(dr.find_element_by_class_name('APP-editor-iframe'))
dr.find_element_by_class_name('nui-scroll').send_keys('hello')
sleep(3)
dr.switch_to.parent_frame()           #  退回到上一层的框架
dr.find_elements_by_class_name('nui-toolbar-item')[0].click()
dr.quit()



