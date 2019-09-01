#!/sur/bin/python
# -*-coding:utf-8-*-


# import requests
# import re
# respose=requests.get('http://www.xiaohuar.com/v/')
# # print(respose.status_code)# 响应的状态码
# # print(respose.content)  #返回字节信息
# # print(respose.text)  #返回文本内容
# urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
# url=urls[5]
# result=requests.get(url)
# mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
#
# video=requests.get(mp4_url)
#
# with open('D:\\b.mp4','wb') as f:
#     f.write(video.content)







import re
import requests
import random
import pymysql
# n = random.randint(0, 36)
# user_agent = [
#     "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
#     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
#     "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
#     "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
#     "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
#     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
#     "UCWEB7.0.2.37/28/999",
#     "NOKIA5700/ UCWEB7.0.2.37/28/999",
#     "Openwave/ UCWEB7.0.2.37/28/999",
#     "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
#     # iPhone 6：
# 	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
# ]
#
# res1 = requests.get('http://desk.zol.com.cn/bizhi/7590_94219_2.html', headers={"User-Agent": user_agent[n]})
#
# html1 = res1.text
# s = re.compile('<li class=".*">\s*<a href="(.*?)">')
# u = re.findall(s, html1)[0]
# xiao_tu_url = 'http://desk.zol.com.cn' + u
# print(xiao_tu_url)
#
# res2 =requests.get(xiao_tu_url)
# html2 = res2.text
# big = re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
# s = re.findall(big, html2)
# print(s)
#
# res3 = requests.get("http://desk.zol.com.cn" + s[0])
# html3 = res3.text
# print(html3)
#
# x = re.compile('<img src="(.*?)">')
# g = re.findall(x, html3)
# print(g)
#
# res2 = requests.get(g[0])
# img = res2.content
# # 保存
# with open('2.jpg', 'wb') as f:
#     f.write(img)




import  requests
import re
#    抓取豆瓣网站的
# class Douban(object):
#     def print_res(self,page):
#         url =f'https://movie.douban.com/top250?start={page}&filter='
#         head ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#         res = requests.get(url=url,headers=head)
#         html = res.content.decode('utf-8')
#         return  html
#     def guolv(self,a):
#         title,lianjie = [],[]
#         patt = re.compile(r'<div class="hd">(.*?)</span>',re.S)
#         items = re.findall(patt,a)
#         for i in items:
#             c = re.compile('<span class="title">(.*)',re.S)
#             w = re.findall(c,i)
#             title.append(w[0])
#         tupian_1 = re.compile('<div class="pic">(.*?)</a>',re.S)
#         bbb = tupian_1.findall(a)
#         for j in bbb:
#             tupian = re.compile('src="https://(.*?).jpg"',re.S)
#             qqq = tupian.findall(j)
#             ccc = 'https://'+qqq[0]+'.jpg'
#             lianjie.append(ccc)
#         return title,lianjie
#     def save_(self,ziyuan):
#         for k,p in  enumerate(ziyuan[1]):
#             res = requests.get(p)
#             hhh = res.content
#             with open(f"{ziyuan[0][k]}.jpg",'wb') as f:
#                 f.write(hhh)
# du = Douban()
# for ppppp in range(1,101,25):
#     htm = du.print_res(ppppp)
#     ziyuan = du.guolv(htm)
#     du.save_(ziyuan)

#  抓取智联招聘信息并保存到excel表中
# import  xlwt
# class Lagou(object):
#     def a(self):
#         url = f'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.99268489&x-zp-page-request-id=8c7d0c9b49ee478387c43ebbab035723-1562659381745-563431&x-zp-client-id=bbea1592-c051-45e6-bbd8-96267436ee2c'
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#         res = requests.get(url=url,headers=head)
#         b = res.text          # res.text  生成的是字符串，正则可以操作字符串
#         # print(b)
#             正则刷选
#         a1 = re.compile(r'"jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S)
#         items = re.findall(a1,b)
#         #print(items)
#         #print(len(items))
#         biao =xlwt.Workbook()
#         biao1 = biao.add_sheet("1")
#         for i in range(len(items)):
#             for j in range(len(items[i])):
#                 biao1.write(i,j,items[i][j])
#         biao.save("智联.xls")
# qq = Lagou()
# qq.a()


#  抓取智联招聘信息，并保存到数据库
# import pymysql
# class Lagou(object):
#     def a(self):
#         url = f'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.99268489&x-zp-page-request-id=8c7d0c9b49ee478387c43ebbab035723-1562659381745-563431&x-zp-client-id=bbea1592-c051-45e6-bbd8-96267436ee2c'
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#         res = requests.get(url=url,headers=head)
#         b = res.text          # res.text  生成的是字符串，正则可以操作字符串
#         # print(b)
#         a1 = re.compile(r'"jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S)
#         items = re.findall(a1,b)
#         return items
#     def ku(self):
#         a1 = self.a()     #  继承上面的方法
#         shujuku = pymysql.connect(                        #  建库
#             host = "192.168.10.16",
#             port = 3306,
#             user = "root",
#             password = "123456",
#             charset = "utf8",
#             database = "aaa"
#         )
#         cur = shujuku.cursor()                         # 游标
#         sq = "create table zl (zhiwu char(20),gongsi char(20),dizhi char(20),gongzi char(20),xueli char(10),gongling char(10) )"
#         cur.execute(sq)
#         for m in  a1:
#             sq1 = f"insert into zl values {m}"
#             cur.execute(sq1)
#         shujuku.commit()
#
# qqq = Lagou()
# qqq.ku()




import  re
import requests
import random
# user_agent = [
#     "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
#     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
#     "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#     "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
#     "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
#     "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
#     "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
#     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
#     "UCWEB7.0.2.37/28/999",
#     "NOKIA5700/ UCWEB7.0.2.37/28/999",
#     "Openwave/ UCWEB7.0.2.37/28/999",
#     "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
#     # iPhone 6：
# 	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
# ]
# n = random.randint(0, 36)
# class A(object):
#     def a(self):
#         a1 = requests.get(f'http://desk.zol.com.cn/bizhi/7599_94349_2.html',headers={"User-Agent": user_agent[n]})
#         b = a1.text
#         b1 = re.compile(r'<li class="show.*?">.*?<a href="(.*?)">',re.S)
#         b2 = re.findall(b1,b)
#         # print(b)
#         a2 = []
#         for i in b2:
#             b3 = 'http://desk.zol.com.cn' + i
#             a2.append(b3)
#         # print(a2)
#         a4 = []
#         for j in a2:
#             # print(j)
#             a3 = requests.get(j)
#             b4 = a3.text
#             b5 = re.compile(r'<img id="bigImg" src="(.*?)" width="960" height="600">')
#             b6 = re.findall(b5,b4)
#             a4.append(b6)
#         # print(a4)
#         for m in range(len(a4)):
#             a5 = requests.get(a4[m][0])
#             b7 = a5.content
#             with open(f'{m}.jpg','wb') as f:
#                 f.write(b7)
#
#
#
# aa = A()
# aa.a()



# a = requests.get('https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.05608290&x-zp-page-request-id=431f781104cb4d2b809e3d80b80e94b6-1563365550047-627013&x-zp-client-id=b40878a2-f677-4485-a6a5-b9648a99c648',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'})
# b = a.text
# a1 = re.compile('"jobName":"(.*?)".*?"company":{"name":"(.*?)".*?"display":"(.*?)".*?"workingExp":{"name":"(.*?)"')
# a2 = re.findall(a1,b)
# print(a2)
# w = pymysql.connect(
#     host="192.168.10.11",
#     user="root",
#     password="123456",
#     charset="utf8",
#     database="python111",
# )
# cur = w.cursor()
# sql1 = "create table a1 (m char(20),m1 char(20),m2 char(20),m3 char(20))"
# cur.execute(sql1)
# for i in range(len(a2)):
#     sql2 = f"insert into a1 values {a2[i]}"
#     cur.execute(sql2)



#第三题
import  os
# a = os.mkdir("aaa")
# with open(r"E:\untitled4\aaa\cc.txt",mode="w",encoding="utf-8")  as f:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             f.write(f"{j}*{i}={i*j}\t")
#         f.write("\n")
# b = os.remove(r"E:\untitled4\a.txt")
# c = os.rmdir("aaa")


# with  open("a.txt",mode="w",encoding="utf-8")    as  f:
#     f.write("zhe,shi,juedu,123\n"*100)

#
# import  pymysql
# class A(object):
#     def __init__(self):
#         self.a=pymysql.connect(
#             host = "192.168.10.11",
#             port = 3306,
#             user = "root",
#             password ="123456",
#             charset = "utf8",
#             database = "python"
#         )
#         self.a1 = self.a.cursor()
#     def c(self):
#         sq1 = "create table a3 (m char(20),m1 char(20),m2 char(20),m3 int(10))"
#         self.a1.execute(sq1)
#     def cc(self):
#         with open("a.txt", mode="r", encoding="utf-8") as f:
#             a = f.read()
#             t = a.strip()
#             b = t.split("\n")
#             for i in range(len(b)):
#                 t = b[1].split(",")
#                 r = tuple(t)
#                 # print(r)
#                 sql2 = f"insert into a3 values {r}"
#                 self.a1.execute(sql2)
#                 self.a.commit()
#
# w = A()
# w.c()
# w.cc()






