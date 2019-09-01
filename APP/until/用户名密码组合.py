#!/sur/bin/python
# -*-coding:utf-8-*-
with open(file=r"E:\APP\data\a.txt",mode="r",encoding="utf-8") as f:
    fb = f.read().split(";")
    # print(fb)

s = []
for i in fb:
    e = i.replace("\n","").split(",")    #  替换之后进行切割
    s.append(tuple(e))
print(s)

