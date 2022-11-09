import TCPTalk
def ServerAPP(ip,port):
    tcp=TCPTalk.TCPtalk(ip,port)
    tcp.ServerU()

if __name__ == '__main__':
    ServerAPP('127.0.0.1',8000)