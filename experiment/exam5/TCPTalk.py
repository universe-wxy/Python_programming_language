import socket
import sys
import threading


class TCPtalk:
    def __init__(self,ip,port):
        self.__ip=str(ip)
        self.__port=int(port)

    def ServerU(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.__ip,self.__port))
            s.listen(10)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print("Waiting connection......")

        while True:
            conn, addr = s.accept()
            buf=conn.recv(1024)
            buf=buf.decode()
            print("Data comes from {}".format(str(addr[0])))
            print("Following message has been received\n{}".format(str(buf)))

    def ClientU(self,data):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.__ip,self.__port))
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        s.send(data.encode())
        print("Data send out successfully")
        s.close()

