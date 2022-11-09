#建立基于TCP协议的网络通信协议
from socket import*
from time import ctime

#客户端代码
Buf=1024
addr=('127.0.0.1',9000)
sc=socket(AF_INET,SOCK_STREAM,0)#创立套接字
sc.connect(addr)#连接至服务器端
data=sc.recv(Buf).decode('utf-8')#监听服务器端传来的待使用信息，例如“欢迎你的到来！”
if data:
    print(data)
while True:
    print("请输入要传输的信息")
    data=input()#向服务器端传输数据
    if data:
        sc.sendall(bytes(data,'utf-8'))#编码后传输数据
        print("信息传输成功")
        data=sc.recv(Buf).decode('utf-8')#接受本客户端上传信息 后 服务器端返回的数据
        if data:
            print(data)
            print("信息接收成功")


