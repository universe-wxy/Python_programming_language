import sys
import os
import socket
import struct
import threading


def socket_server():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(('127.0.0.1',5678))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Waiting connection......")

    while True:
        conn,addr=s.accept()
        t=threading.Thread(target=deal_data,args=(conn,addr))
        t.start()

def deal_data(conn,addr):
    print('Accept new connection from {0}.'.format(addr))
    conn.send('The server is successfully connected.'.encode('utf-8'))

    while True:
        filein_size=struct.calcsize('128sl')
        buffer=conn.recv(filein_size)
        if buffer:
            file_name,file_size=struct.unpack('128sl',buffer)
            fn=file_name.strip(b'\00').decode()
            print("Received filename changed into {0},filesize {1}".format(str(fn),file_size))
            recved_size=0
            fp=open('./server_document/'+str(fn),'wb')
            print('Staring receiving......')
            while not recved_size==file_size:
                if file_size-recved_size>1024:
                    data=conn.recv(1024)
                    recved_size+=len(data)
                else:
                    data=conn.recv(file_size-recved_size)
                    recved_size=file_size
                fp.write(data)
            print('Transmission Complete......')
        conn.close()
        break

if __name__ == '__main__':
    socket_server()