#!/sur/bin/python
# -*-coding:utf-8-*-


#        客户端
import socket
ip_port = ('127.0.0.1',888)           #指定客户端的ip地址，和端口号
c=socket.socket()                      #创建套接字，目的接收服务器发送的数据
c.connect(ip_port)                     #连接服务器
while True:
    #  发送数据到服务器，接收服务器数据
    t =input("输入发送的信息")
#设置一个条件跳出死循环
    if t =="1":
        break
    else:
        # 发送信息到服务端
        print(f"客户端向服务器发送的信息：")
        c.sendall(t.encode())
        #处理服务器已经发送到客户端上的信息
    s_data = c.recv(1024).decode("utf-8")
    print(s_data)

#关闭连接
c.close()
