#!/sur/bin/python
# -*-coding:utf-8-*-



#   python 发送电子邮件   使用到的模块    smtplib   email
import  smtplib
from email.mime.text  import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置服务器所需要的信息
mail_host = "smtp.163.com"                                      #  邮件服务器地址
mail_user = "guohg18991002302@163.com"                            #  用户名
mail_pass = "guo18991002302"                                   #客户端授权码或者密码
mail_port = 465                                                    #设置服务器端口号
sender = "guohg18991002302@163.com"                                           #  邮件发送方的地址
receviers = ["guo6390259@qq.com"  ]                                    #  邮件接收方的地址
#  设置邮件信息如下
a = "python测试邮件"                   #  设置邮件主题
# a1 = "这是我使用python发送的邮件"       # 设置邮件正文
# s = MIMEText(a1,'plain','utf-8')       #三个参数：第一个为文本内容，第二个设置文本格式，第三个设置编码方式
# #  发送邮件是填写收件人，发件人，主题
# # header（）： 填写邮件头部
# s['From'] = Header(sender)                              #  发送方信息
# s["To"] = Header(str(";".join(receviers)))       # 接收方信息
# s["Subject"] = Header(a)                         #  主题绑定
# #  登录并发送邮箱
# try:
#     # 第一步，登录到自己的邮箱   #  一种是不使用授权密码
#     s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#     # 第二步，输密码登录邮箱
#     s1.login(user=mail_user,password=mail_pass)
#     # 第三步,发送邮件，as_string()    以字符串的形式发送出去
#     s1.sendmail(sender,receviers,s.as_string())
#     #  第四步，发送邮件之后退出邮箱
#     s1.quit()
#     print("发送成功，退出邮箱")
# except smtplib.SMTPException as e :
#     print("登录失败")                    #   错误类


#添加附件，要使用一个MIMEMultipart类， 作用是处理正文及附件添加到邮件里
e =  MIMEMultipart()
e['From'] = Header(sender)                              #  发送方信息
e["To"] = Header(str(";".join(receviers)))       # 接收方信息
e["Subject"] = Header(a)                         #  主题绑定
#  使用html格式的正文内容，添加附件
with open('abc.html','r',encoding='utf-8')  as f:
    connect = f.read()
#  设置html格式参数
patr1 = MIMEText(connect,'html','utf-8')
#   以下都是附件代码
with  open('c.txt','r',encoding='utf-8')  as  h:                   #添加一个txt文本附件
    connect1 = h.read()
patr2 = MIMEText(connect,'plain','utf-8')           #设置txt参数
# 附件设置内容类型，方便起见，设置为二进制流
patr2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
patr2['Content-Disposition'] = 'attachment;filename="c.txt"'
with open('a.png','rb') as fp:   #添加图片附近
    picture = MIMEImage(fp.read())
# 附件设置内容类型，方便起见，设置为二进制流
picture['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
picture['Content-Disposition'] = 'attachment;filename="1.png"'

#  拼接
#  将html添加到邮件里， attach（添加的内容）
e.attach(patr1)
e.attach(patr2)
e.attach(picture)
#  登录并发送
try:
    # 第一步，登录到自己的邮箱   #  一种是不使用授权密码
    s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)
    # 第二步，输密码登录邮箱
    s1.login(user=mail_user,password=mail_pass)
    # 第三步,发送邮件，as_string()    以字符串的形式发送出去
    s1.sendmail(sender,receviers,e.as_string())
    #  第四步，发送邮件之后退出邮箱
    s1.quit()
    print("发送成功，退出邮箱")
except smtplib.SMTPException as e:
    print("登录失败")                    #   错误类



















"""
#  用面向对象写出发送邮件
class A(object):
    mail_host = "smtp.163.com"  # 邮件服务器地址
    mail_user = "guohg18991002302@163.com"  # 用户名
    mail_pass = "guo18991002302"  # 客户端授权码或者密码
    mail_port = 465  # 设置服务器端口号
    sender = "guohg18991002302@163.com"  # 邮件发送方的地址
    def __init__(self,jieshou,zhuti,zhengwen):
        self.jieshou = jieshou
        self.zhuti = zhuti
        self.zhengwen = zhengwen
        self.receviers = [self.jieshou]             #  邮件接收方
        self.a = self.zhuti                         #   主题
        self.a1 = self.zhengwen                     #  正文
        self.s = MIMEText(self.a1,'plain','utf-8')
    def fa(self):
        self.s['From'] = Header(self.sender)                  # 发送方信息
        self.s["To"] = Header(str(";".join(self.receviers)))  # 接收方信息
        self.s["Subject"] = Header(self.a)                     # 主题绑定
        try:
            s1 = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)    # 第一步，登录到自己的邮箱
            s1.login(user=self.mail_user, password=self.mail_pass)             # 第二步，输密码登录邮箱
            s1.sendmail(self.sender, self.receviers, self.s.as_string())       # 第三步,发送邮件，as_string()
            s1.quit()                                                          #  第四步，发送邮件之后退出邮箱
            print("发送成功，退出邮箱")
        except smtplib.SMTPException as e:
            print("登录失败")                                                   # 错误类
qq = A("guo6390259@qq.com","python测试邮件","这是我使用python发送的邮件" )
qq.fa()
"""












