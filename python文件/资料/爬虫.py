#!/sur/bin/python
# -*-coding:utf-8-*-

#            自动化      spider    网络蜘蛛  根据自己制定的规则，模拟浏览器批量下载网络中的资源
#            有目的的获取网络中的资源          scrapy   爬虫框架
#     分两类     聚焦爬虫： 只针对某个网络进行的资源爬取
                # 搜索爬虫： 针对全网络进行的资源爬取   （百度搜索引擎）
              #   爬虫使用到的库：  requests /  urllib2 /  urllib3 /  httpclient
#                 删选数据的模块：re /bs4 /xpsth
#         #    import ison   模块     ison.load(想转的内容)，   将json转化为python字典
#           #                         ison.dumps(想转的内容)    将python转化为json字符串
import requests              #  访问服务器用的模块
import  re
import random                # 获取随机数模块
# d = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# # 第一步  发送URL请求
# req = requests.get("https://www.fpzw.com/xiaoshuo/88/88413",headers=d)
# # 接 收html文本
# res = req.content.decode('gbk')
# print(res)
# #  获取小说文本的内容
# s1 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
# s2 = re.compile('</h2>(.*)</h2>')
# biaoti = re.findall(s2,res)
# neirong= re.findall(s1,res)
# print(biaoti)
# print(neirong)

#   保存

# class As(object):
#     d = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"}
#     def __init__(self,yuming):
#         self.yuming = yuming
#         req = requests.get(self.yuming,headers=self.d)     #发送URL请求
#         res = req.content.decode("gbk")      #接收html文本
#         s3 = re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')   #使用正则表达式整理目录
#         self.u1 = re.findall(s3,res)    #输出为元素为元组的列表
#     def adf(self):
#         for i in self.u1:
#             ur = f'{self.yuming}{i[0]}.html'   # i[0]为 网址中的各章节不同部位     #发送URL请求
#             mu = i[1]
#             req = requests.get(ur,headers=self.d)        #接收html文本
#             res = req.content.decode("gbk")         #解析文本
#             w2 = re.compile("&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>")
#             ne2 = re.findall(w2,res)
#             ne = ne2[0]
#             nei = ne.replace("<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;","\n")
#             with open(file="棋祖.txt",mode="a",encoding="utf8") as f:
#                 f.write(mu)
#                 f.write("\n")
#                 f.write(nei)
#                 f.write("\n\n")
#             print(f"已成功导入{mu}")
# a = As("https://www.fpzw.com/xiaoshuo/88/88413/")
# a.adf()

n = random.randint(0,36)
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]

class Zol(object):
    #  请求URL
    def get_url(self):
        res = requests.get("http://desk.zol.com.cn/bizhi/7590_94219_2.html",headers={"User_Agent":user_agent[n]})
        # 获取html
        html = res.text
        return html
    #从html文本中找我们想要的资源
    def res(self):
        a = self.get_url()     #  None    _——html
        #print(a)
        #匹配大图的正则
        big=re.compile('<li class=".*">\s*<a href="(.*?)">')
        l = re.findall(big,a)
        # print(l)
        c = []
        for i in l:
            l1 = "http://desk.zol.com.cn" + i
            c.append(l1)
        # print(c)
        return c
    def get(self):
        a1 = self.res()
        c1 = []
        for i in a1:
            res1 = requests.get(i)
            html1 = res1.text
            print(html1)
            # big1 = re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
            # l1 = re.findall(big1, html1)
            # c1.append(l1)
        # print(c1)
        #return  c1
    # def get1(self):
    #     a2 = self.get()
    #     c3 = []
    #     for i in a2:
    #         if len(i):
    #             l2 = "http://desk.zol.com.cn" + i[0]
    #             c3.append(l2)
    #     #print(c3)
    #     return c3
    # def get2(self):
    #     a3 = self.get1()
    #     c4 = []
    #     for i in a3:
    #         res2 = requests.get(i)
    #         html2 = res2.text
    #         big2 = re.compile('<img src="(.*?)">')
    #         l3 = re.findall(big2,html2)
    #         c4.append(l3)
    #     # print(c4)
    #     return  c4
    # def get3(self):              #  下载
    #     a4 = self.get2()
    #     o = 0
    #     for i in a4:
    #         res3 = requests.get(i[0])
    #         p = res3.content
    #         with open(f"{o}.jpg","wb") as f:
    #             f.write(p)
    #             o = o+1

z = Zol()
# z.res()
z.get()













#print(len(user_agent))
# class ZOL(object):
#     #请求url
#     def get_url(self):
#         res = requests.get('http://desk.zol.com.cn/bizhi/7590_94219_2.html', headers={"User_Agent":user_agent[n]})
#         #获取html文本
#         html=res.content.decode('gb2312')
#         s = re.compile('<li class=".*">\s*<a href="/bizhi/7590(.*?)">')
#         u = re.findall(s, html)
#         j=[]
#         for i in u:
#             j.append('http://desk.zol.com.cn/showpic/1920x1200'+i)
#         print(j)
#         return  j
#     # 从html文本中找我们要的
#     def get_big_img_url(self):
#         a=self.get_url()    #none --html文本
#     def get_big_img(self):
#         a1 = self.get_url()
#         c=0
#         for i in a1:
#             res=requests.get(i, headers={"User_Agent":user_agent[n]})
#             html = res.content.decode('gb2312')
#             s=re.compile('<img src="(.*?)"')
#             img_url=re.findall(s,html)
#             # print(img_url)
#             #下载图片
#             res2=requests.get(img_url[0])
#             img=res2.content
#             #print(img)
#             #保存
#             c+=1
#             with open(f"{c}.jpg",'wb') as f:
#                 f.write(img)
# z=ZOL()
# z.get_url()
#z.res()
# z.get_big_img_url()
#z.get_big_img()
