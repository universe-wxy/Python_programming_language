import socket
import os
import sys
import struct

def socket_client():
    #创建套接字对象并连接指定IP
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('127.0.0.1',5678))
    except socket.error as msg:
        print(msg)
        sys.exit(10)
    print(s.recv(1024))


    filepath=input("请输入要传输的文件地址:").strip()
    if os.path.isfile(filepath):
        fhead=struct.pack('128sl',os.path.basename(filepath).encode('utf-8'),os.stat(filepath).st_size)
        s.send(fhead)
        fp=open(filepath,'rb')
        while True:
            data=fp.read(1024)
            if not data:
                print('{0} file send over.'.format(os.path.basename(filepath)))
                break
            s.send(data)
    else:
        print("不存在该文件")
    s.close()

if __name__ == '__main__':
    socket_client()