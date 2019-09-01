#!/sur/bin/python
# -*-coding:utf-8-*-
import pytest
import requests
from unitl.数据 import s
from unitl.日志 import get_logger
from unitl.数据 import s1

log = get_logger(filename='test_2.py')


@pytest.mark.parametrize('x,y',s)
def test_1(jk,x,y):
    # querystring = {"key":'%s' %(x), "chars":'%s' %(y)}
    querystring = {"key":f'{x}', "chars":f'{y}'}
    # querystring['key'] = x
    # querystring['chars'] = y
    log.info("请求成功")
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "958b0032-f411-4301-9ac0-9fec4fe2d183,575a7562-b6aa-4072-adbb-eff10654bbed",
        'Host': "v.juhe.cn",
        'Cookie': "aliyungf_tc=AQAAANrPp1wntwYAKmU9c6QAXatjnaBa",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", jk, headers=headers, params=querystring)

    print(response.json())
    log.info("【正确的key】，正确的【chars】")
    assert     response.json()['reason']  == "success"

@pytest.mark.parametrize('m,n',s1)
def test_2(jk,m,n):
    # querystring = {"key":'%s' %(x), "chars":'%s' %(y)}
    querystring = {"key":f'{m}', "chars":f'{n}'}
    # querystring['key'] = x
    # querystring['chars'] = y
    log.info("请求成功")
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "958b0032-f411-4301-9ac0-9fec4fe2d183,575a7562-b6aa-4072-adbb-eff10654bbed",
        'Host': "v.juhe.cn",
        'Cookie': "aliyungf_tc=AQAAANrPp1wntwYAKmU9c6QAXatjnaBa",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", jk, headers=headers, params=querystring)

    print(response.json())
    log.info("【key】与【chars】错误")
    assert     response.json()['result']  ==  None
