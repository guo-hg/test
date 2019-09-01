#!/sur/bin/python
# -*-coding:utf-8-*-
from time import sleep
from selenium import webdriver






dr = webdriver.Chrome()
dr.get("https://www.jd.com/")
dr.maximize_window()
print(dr.title)
print(dr.current_url)
a = dr.find_element_by_class_name('logo_tit_lk').text
print(a)
