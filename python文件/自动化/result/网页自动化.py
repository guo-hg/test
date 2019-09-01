#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep



dr = webdriver.Chrome()



# 访问网址
# dr.get("https://www.ctrip.com")


# 获取访问网址的标题
# print(dr.title)

# 获取访问的网址
# print(dr.current_url)

# 设置浏览器窗口的大小
# dr.set_window_size(width=800,height=1000)             #宽800，高1000
#
# 设置浏览器的位置
# dr.set_window_position(100,200)

# 最大化浏览器
# dr.maximize_window()                      # 最大化
# dr.minimize_window()                      # 最小化




# dr.maximize_window()


# sleep(2)



'''
dr.get("https://www.jd.com")
print(dr.title)
dr.maximize_window()

# 回退到上一次的页面
dr.back()
sleep(2)

#前进到第二个页面

dr.forward()
sleep(2)

a = dr.current_window_handle #  获取当前位置的句柄
print(a)


dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a').click()    #  点击秒杀
sleep(3)

a = dr.window_handles
print(a)

dr.switch_to.window(a[-1])

print(dr.title)
dr.find_element_by_xpath('//*[@id="skmu"]/div/div[1]/ul/li[2]/a').click()

'''







'''
核心：定位
1.id；2.class_name；3.name；4.link_text;5;tag_name;6.xpath;7.css;8.partial_link_text

1、id定位  动作 1.click（）——点击        2.send_keys（）   输入值

dr.find_element_by_id("kw").send_keys("python")
dr.find_element_by_id("su").click()

 2、class定位  只要class值唯一，就可以定位
dr.find_element_by_class_name("class属性的值")

3、name   指的是name属性
dr.find_element_by_name("tj_settingicon").click()

4、 link_text  文本定位    必须保证文本唯一
dr.find_element_by_link_text("新闻").click()
sleep(3)
5、partial_link_text      模糊文本
dr.find_element_by_partial_link_text("加拿大驻香港领事馆").click()
sleep(3)

6.tag_name     标签定位，通常用来定位一组对象

7、  xpath   路径标记语言       绝对路径，相对路径   通常用来标记可扩展语言(xml),内容和html一样
  xml  作用：用来储存数据
dr.find_element_by_xpath('//*[@id="u_sp"]/a[1]').click()

8、css   层叠样式表
dr.find_element_by_css_selector('#u_sp > a:nth-child(1)').click()


打开网页的代码添加一句
dr.get("")
sleep(2)
dr.switch_to.frame("login_frame")

 定位一组对象：同时定位到多个元素，结果是个列表
 层级定位：先定位一个大范围，再从大范围定位元素
dr.父元素.子元素.动作
父元素必须是唯一的，     子元素可以是一组，可以是唯一的
sleep(3)
ww = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name("option")
# print(len(ww))
for i in ww:
    i.click()
    sleep(3)
    print(i.text)
a = dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name("option")
for i in a:
    i.click()
    sleep(3)
    print(i.text)
'''






# iframe: 内嵌框架
#swith_to 切换框架，切换框架时只可以用name和ID的值，如果没有ID和name的情况下，先定位到框架，在切换

# dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="login_frame"]'))

# dr.switch_to_default.content()    #   退出到第一层页面
# dr.switch_to.parent_frame()         #   退出到上一层框架




# dr.get("https://qzone.qq.com/")
# print(dr.title)
# print(dr.current_url)
# dr.maximize_window()
# dr.switch_to.frame("login_frame")  # 内嵌框架
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('452286292')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('guo18991002302..')
# sleep(3)
# dr.find_element_by_class_name('login_button').click()
# sleep(3)


# 浏览器管理窗口的原理:
# 浏览器会对每个打开的窗口生成一个唯一标识这个窗口的句柄
# 谷歌产生的句柄是一堆字符串，火狐产生的句柄是一堆数字

#
dr.get('https://www.douban.com')
sleep(2)

#  获取当前所在窗口的句柄
dd = dr.current_window_handle
print(dd)
dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
sleep(3)
#
# # 获取所有窗口的句柄
dd = dr.window_handles
print(dd)
#
# # 切换窗口
dr.switch_to.window(dd[-1])
#
print(dr.title)





'''
dr.get("http://www.ifeng.com")
sleep(3)


# 执行JavaScript函数
# 用法:  1.滚动条滚动到指定位置
dd = dr.find_element_by_link_text('中国民间智库第八次发表日本军力评估报告')
sleep(3)
dr.execute_script('arguments[0].scrollIntoView();',dd)
# 用法2：更改页面的高度滑动滚动条，10000指的是高度

for i in range(1,10000,200):
    js = f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
dr.quit()
'''









"""
dr.get('file:///C:/Users/guo-hg/Desktop/abc.html')
sleep(3)
dr.find_element_by_xpath('/html/body/button').click()
sleep(3)

#   处理弹出框    alert弹出框
#   将控制器切换到弹出框

ww = dr.switch_to_alert()
print(ww.text)                         # 获取弹出框上的文本
ww.send_keys("hello world")            # 给弹出框输入内容
ww.accept()                            # 点击弹出框上的确定
ww.dismiss()                           # 点击弹出框上的取消

"""


import selenium.webdriver.support.ui as ui          # 智能等待模块
from selenium.webdriver.common.action_chains import ActionChains         # 拖拽模块
# dr.get("http://qzone.qq.com")
# sleep(3)   #  强制等待
# 智能等待
# until = ui.WebDriverWait(dr,10)                     #  设置智能等待


#  定位要出现的元素
# until.until(lambda dr: dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a').is_displayed())  #is_displayed   是否出现
# dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a').click()


# ww = dr.find_elements_by_class_name('cate_menu_item')
# # print(len(ww))
#
# for i  in ww:
#     # ActionChains 动作链   作用：控制鼠标移动到某个元素的中心点
#     ActionChains(dr).move_to_element(i).perform()    #perform   执行
#     sleep(2)



# dr.switch_to.frame('login_frame')
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('124522534')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('344354315')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
# dr.switch_to.frame('tcaptcha_iframe')
# ww = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')               #  起始位置
# ActionChains(dr).drag_and_drop_by_offset(ww,185,0).perform()                   #  进行拖拽




