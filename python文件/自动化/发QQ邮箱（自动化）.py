#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


dr = webdriver.Chrome()
dr.get("https://mail.qq.com")
print(dr.title)        # 获取标题
sleep(3)
print(dr.current_url)  # 获取网址
dr.maximize_window()    # 窗口最大化
sleep(3)
dr.switch_to.frame("login_frame")
sleep(3)
dr.find_element_by_id("switcher_plogin").click()        #  账号密码登录
sleep(5)
dr.find_element_by_id("u").click()                      # 点击账号
sleep(5)
dr.find_element_by_id("u").send_keys("452286292")        #输入账号
sleep(5)
dr.find_element_by_id("p").click()                       # 点击密码
sleep(5)
dr.find_element_by_id('p').send_keys("guo18991002302..")  #输入密码
sleep(5)
dr.find_element_by_id("login_button").click()             # 点击登录
sleep(5)
dr.find_element_by_link_text("写信").click()               # 点击写信
sleep(5)
dr.switch_to.frame('mainFrame')
sleep(2)
for i  in  range(5):
    dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys("1778109280@qq.com")
    sleep(3)
    dr.find_element_by_xpath('//*[@id="subject"]').click()
    dr.find_element_by_xpath('//*[@id="subject"]').send_keys("web自动化测试")
    sleep(5)
    dr.switch_to.frame(dr.find_element_by_class_name('qmEditorIfrmEditArea'))
    sleep(5)
    dr.find_element_by_xpath('/html/body').send_keys("这是我给你发的第一封信")
    sleep(5)
    dr.switch_to.parent_frame()
    dr.find_element_by_name('sendbtn').click()  # 发送
    sleep(5)
    # dr.switch_to.frame('mainFrame')
    dr.find_element_by_id('btnagainl').click()
sleep(3)
dr.quit()