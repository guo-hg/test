#!/sur/bin/python
# -*-coding:utf-8-*-
import requests
import pytest
from appium import webdriver

'''
with open(file=r"E:\接口自动化\data\a.txt",mode="r",encoding="utf-8") as f:
    a = f.read()

    a1 = a.split(";")
    print(a1)
    a2 = []
    for i in a1:
        a2.append(i.replace("\n",""))
    print(a2)


@pytest.fixture(scope='function',params=a2)
def ni(request):
    return request.param
def test_1(ni):
    url = "http://v.juhe.cn/xianxing/index"

    payload = f"key=f3973aa74b35a3b8a3bc04b695e243d4&city={ni}"
    headers = {
        'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA,yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA; aliyungf_tc=AQAAANrPp1wntwYAKmU9c6QAXatjnaBa",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "78a7eedb-2785-4f50-85a4-ffd98c509ee2,500e1c16-f4a3-419c-9244-672be2c2f963",
        'Host': "v.juhe.cn",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "49",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)
    # try:
    #     assert  "查询成功" in response.json()
    # except:
    #     assert  "错误的请求KEY" in response.json()["msg"]

'''



#
# with open(file=r'E:\接口自动化\data\b.txt',mode='r',encoding='utf-8') as f:
#     # a = f.read()
#     # print(a)
#     a1 = f.read().split(";")
#     print(a1)
#
# s = []
# for i in a1:
#     k = i.replace('\n','').split(",")
#     s.append(tuple(k))
# # print(s)
#
# @pytest.mark.parametrize('x,y',s)
# def test_1(x,y,jk):
#     # url = "http://v.juhe.cn/xianxing/index"
#
#     payload = f"key={x}&city={y}"
#     headers = {
#         'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA,yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA; aliyungf_tc=AQAAANrPp1wntwYAKmU9c6QAXatjnaBa",
#         'Content-Type': "application/x-www-form-urlencoded",
#         'User-Agent': "PostmanRuntime/7.15.2",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "78a7eedb-2785-4f50-85a4-ffd98c509ee2,500e1c16-f4a3-419c-9244-672be2c2f963",
#         'Host': "v.juhe.cn",
#         'Accept-Encoding': "gzip, deflate",
#         'Content-Length': "49",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#     }
#
#     response = requests.request("POST", url=jk, data=payload, headers=headers)
#
#
#     print(response.text)
#












