#!/sur/bin/python
# -*-coding:utf-8-*-
with open(file=r"E:\QQ\data\login.txt",mode="r",encoding="utf-8") as fb:
    # fb.read()
    datas = fb.read().split(";")
    print(datas)


s = []
for i in datas:
    k = i.replace('\n','').split(",")
    s.append(tuple(k))
# print(s)

