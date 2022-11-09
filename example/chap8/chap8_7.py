#使用基于TCP的socket套接字模块编写一个网络通信程序，实现客户与服务器的交互计算。其中，客户端将三角形的三边长发给服务器，服务器计算出三角形的面积再把结果返沪给客户端

"""
#服务器端
from socket import*
from time import ctime
from math import*
def triangle(a,b,c):
    s=(a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))
addr=('127.0.0.1',8000)#ip与端口
ss=socket(AF_INET,SOCK_STREAM ,0 )#创建套接字
ss.bind(addr)
ss.listen(20)

while True:
    print("等待客户连接..\r\n")
    cs,caddr=ss.accept()
    print("连接来自于: ",caddr)
    data="欢迎你的到来！\r\n"
    cs.sendall(bytes(data,'utf-8'))#发送”发送你的到来！“
    data=cs.recv(1024).decode('utf-8')#接受来自客户端的信息
    print("信息接收成功")
    if not data:
        break
    print("三角形三边长为:",data)#显示接受的客户端信息
    sides=data.split(',')#分割
    cs.sendall(bytes(''+str(triangle(float(sides[0]),float(sides[1]),float(sides[2]))),'utf-8'))
    print("信息传输成功")
    cs.close()
ss.close()
"""



#客户端
from socket import*
from time import ctime
from math import*

s=socket(AF_INET,SOCK_STREAM ,0)
s.connect(('127.0.0.1',8000))
data=s.recv(1024).decode('utf-8')#监听来自服务器端的准备信息
if data:
    print("信息接收成功")
    print(data)
a = input("请输入边长a:\r\n")
b = input("请输入边长b:\r\n")
c = input("请输入边长c:\r\n")
data=a+','+b+','+c
if data:
    s.sendall(bytes(data,'utf-8'))#传输边长信息
    print("数据传输成功")
    data=s.recv(1024).decode('utf-8')#再次接受来自服务器端 传回的三角形面积
    if data:
        print('信息接收成功')
        print('三角形面积为:',data)
    s.close()




