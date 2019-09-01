#!/sur/bin/python
# -*-coding:utf-8-*-
from selenium import webdriver
import  pytest
from  time import  sleep
import allure

# 情咖web
@pytest.fixture(scope='module')
def qingka():
    dr = webdriver.Chrome()
    dr.get("http://www.qingka.fm/")
    dr.maximize_window()
    return dr



