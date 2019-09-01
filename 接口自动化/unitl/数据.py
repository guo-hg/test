#!/sur/bin/python
# -*-coding:utf-8-*-
with open(file=r"E:\接口自动化\data\b.txt",mode="r",encoding='utf-8') as f:
# a = f.read()
    # print(a)
    a1 = f.read().split(";")
    # print(a1)

s = []
for i in a1:
    k = i.replace('\n','').split(",")
    s.append(tuple(k))
print(s)


with open(file=r"E:\接口自动化\data\a.txt",mode="r",encoding='utf-8') as f1:
# a = f.read()
    # print(a)
    a1 = f1.read().split(";")
    # print(a1)

s1 = []
for i in a1:
    k = i.replace('\n','').split(",")
    s1.append(tuple(k))
print(s1)