import socket
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
host="127.0.0.1"#IP地址
port = 8000#端口
while True:
    print("请输入要发送的信息")
    msg=input()
    if not msg:#当输入为空时，跳出输出，发送信息
        break
    s.sendto(msg.encode('utf-8'),(host,port))#将信息编码为bytes类型，发送至设定的ip与端口的客户端
    print("信息发送成功")
s.close()
"""
c=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
c.bind(('127.0.0.1',8000))#绑定到该接口与ip,bind只能连接到一个接口，故此处需要用双重()
print("客户端已经链接")
while True:
    data,addr=c.recvfrom(1024)#接受最大为1024个字节的信息
    if not data:
        print("client has exited!")
        break
    print("信息接收成功")
    Data = data.decode('utf-8')#对传输过来的经过encode数据进行decode解码，转化为str类型
    print("receover:",Data,'from',addr)
c.close()
"""