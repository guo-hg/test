#!/sur/bin/python
# -*-coding:utf-8-*-
import socket
ip_port = ("127.0.0.1",999)   # 指定服务器的ip地址，端口号
s = socket.socket()           # 建立一个套接字，目的是为了服务器向客户端传输消息
s.bind(ip_port)               #  绑定服务器及端口号
s.listen(10)                  # 设置最大连接数
print("启动socket服务，等待客户端连接...")
corn,address = s.accept()              #  持续开启服务，直到手动关闭
while True:
    c = corn.recv(1024).decode("utf-8")  #  接收客户端发送的消息
    print(f"客户端发送的消息是{c}")
    t = input("输入向客户端发送的消息：")
    if t == "1":
        print("关闭服务器")
        break
    else:
        corn.send(t.encode(encoding="utf-8"))
s.close()
