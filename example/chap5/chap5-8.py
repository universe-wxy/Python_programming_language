pme=set()

def pm():
    N=int(input("请输入待验证的偶数n(n>2):"))
    while N<3 or N%2==1:
        print('不符合要求！')
        N=int(input("请输入待验证的偶数n(n>2):"))
    for i in range(2,N+1):
        pme.add(i)
    for i in range(2,N+1):
        if i in pme:
            for k in range(2*i,N+1,i):
                if k in pme:
                    pme.remove(k)
    for e in pme:
            f=N-e
            if f>=e and f in pme:
                print(N,'=',e,'+',f)

pm()