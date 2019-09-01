#!/sur/bin/python
# -*-coding:utf-8-*-
import socket
ip_port = ("127.0.0.1",999)
c = socket.socket()
c.connect(ip_port)
while True:
    t = input("输入发送的消息：")
    if t == "1":
        break
    else:
        print(f"服务器向客户端发送的信息是：")
        c.sendall(t.encode())
        # 处理服务器已经发送到客户端上的信息
    s_data = c.recv(1024).decode("utf-8")
    print(s_data)
c.close()