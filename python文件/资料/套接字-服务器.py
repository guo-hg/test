#!/sur/bin/python
# -*-coding:utf-8-*-



#      作用： 完成两个或者多个应用程序之间的数据传输     使用的模块   socket
import  socket
#   服务端

ip_port = ('127.0.0.1',888)                        #指定服务器的ip地址，监听端口号
s = socket.socket()                                #建立一个套接字，为了服务器和客户端传输信息  默认tcp
s.bind(ip_port)                                    # 绑定服务器地址和端口号
s.listen(5)                                        #设置最大连接数
print("启动socket服务，等待客户端连接...")         #提示服务端已经开始的信息
conn,address = s.accept()                           # socket  自动处理拥塞控制   accept()，持续开启服务，一直到手动关闭
                                                    #  conn  客户端建立的连接   address客户端的IP地址和其随机端口号
while True:
    c_data = conn.recv(1024).decode("utf-8")       #  接收客户端发送的数据
    print(f"客户端向服务器发送的内容是{c_data}")
#    服务器发送数据到客户端
    t =input("输入发送到客户端的信息")
    if t=="1":
        print("关闭服务器")
        break
    else:
        #  发送信息给客户端。 1，先找到客户端，2，使用sendall 3，
        conn.send(t.encode(encoding='utf-8'))
s.close()