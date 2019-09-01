#!/sur/bin/python
# -*-coding:utf-8-*-
import json
import requests
#
# a = {'name':123,'age':456}
# print(a)
# print(type(a))
# # 将字典装换成json字符串
# b = json.dumps(a)
# print(b)
# print(type(b))
#
# # 将json字符串转换成字典
#
# c = json.loads(b)
# print(c)
# print(type(c))


url = 'https://www.amap.com/service/poiTipslite?&city=410200&geoobj=114.245317%7C34.754749%7C114.547441%7C34.844963&words=ken'
bb = requests.get(url)
cc = bb.json()
print(cc)