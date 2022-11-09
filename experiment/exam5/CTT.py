import TCPTalk
def ClientAPP(ip,port,data):
    tcp=TCPTalk.TCPtalk(ip,port)
    tcp.ClientU(data)

if __name__ == '__main__':
    ClientAPP('127.0.0.1',8000,'This is the python examination')