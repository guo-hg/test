#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import ui    # 智能等待
from selenium.webdriver.common.action_chains import ActionChains    #拖拽模块


dr = webdriver.Chrome()                        # dr相当于控制器


'''
dr.get('http://qzone.qq.com')
print(dr.title)                                 #网址标题
print(dr.current_url)                           #网址地址
dr.maximize_window()                            #窗口最大化
dr.switch_to.frame('login_frame')               #切换框架


ww = ui.WebDriverWait(dr,20)                     #设置智能等待
# 等待元素出现
ww.until(lambda dr: dr.find_element_by_id('switcher_plogin').is_displayed())


dr.find_element_by_id('switcher_plogin').click()     #  点击账号密码登录

dr.find_element_by_xpath('//*[@id="u"]').click()
dr.find_element_by_xpath('//*[@id="u"]').send_keys('3005123143')

dr.find_element_by_xpath('//*[@id="p"]').send_keys('49544dt234')

dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(3)
ww = dr.find_element_by_id('tcaptcha_drag_button')                              #  起始位置
ActionChains(dr).drag_and_drop_by_offset(ww,185,0).perform()                   #  进行拖拽

'''

# 执行JavaScript函数
dr.get('https://www.jd.com/')
print(dr.title)
print(dr.current_url)
dr.maximize_window()
sleep(3)
# 执行javas函数，第一种方法：滚动条滚动到指定函数
# ww = dr.find_element_by_id('J_seckill')
# sleep(3)
# dr.execute_script('arguments[0].scrollIntoView();',ww)



#  第二种方法：滚动条按规律进行滚动
# for i in range(1,10000,200):
#     js = f"var q=document.documentElement.scrollTop={i}"
#     dr.execute_script(js)
#     sleep(2)
# dr.quit()

#
# dd = dr.current_window_handle          # 获取当前窗口的句柄
# print(dd)
# dr.find_element_by_xpath('//*[@id="navitems-group2"]/li[2]/a').click() # 跳转至你要点击的页面
# sleep(3)
# dd = dr.window_handles                 # 获取所有窗口的句柄
# print(dd)
# dr.switch_to.window(dd[-1])             # 将鼠标切换到跳转之后的页面
# print(dr.title)                         # 打印标题

# ww = dr.find_elements_by_class_name('cate_menu_item')
# for i in ww:
#     print(i.text)
#     # ActionChains 动作链   作用：控制鼠标移动到某个元素的中心点
#     ActionChains(dr).move_to_element(i).perform()    #perform   执行
#     sleep(2)






#  跳转界面切换句柄
# dd = dr.current_window_handle          # 获取当前窗口的句柄
# print(dd)
# dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[4]/a[1]').click() # 跳转至你要点击的页面
# sleep(3)
# dd = dr.window_handles                 # 获取所有窗口的句柄
# print(dd)
# dr.switch_to.window(dd[-1])             # 将鼠标切换到跳转之后的页面
# print(dr.title)                         # 打印标题
# a = dr.find_element_by_xpath('//*[@id="logo-2014"]/a').text
# print(a)