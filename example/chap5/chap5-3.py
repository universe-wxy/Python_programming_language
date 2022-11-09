def isVIP(L):
    if len(L)!=4:
        return False
    for i in range(4):
        if L[i].isdigit()==False or int(L[i])<0 or int(L[i])>255:
            return False
    return True

def _10to2(num):
    res=""
    while True:
        res=str(num%2)+res
        num=num//2
        if num==0:
            break
    while len(res)<8:
        res='0'+res
    return res

def _10to2(num):
    s=bin(num)
    res=s[2:len(s)+1].rjust(8,'0')
    return res

def main():
    ipS=input('input IP:')
    L=ipS.split('.')
    while not isVIP(L):
        print("IP is error!")
        ipS=input('input IP,again:')
        L=ipS.split('.')
    s=""
    for i in range(4):
        s=s+' '+_10to2(int(L[i]))
    print(s)
main()

