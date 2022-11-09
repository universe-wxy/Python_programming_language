def gmn(m):
    mn={1:"January",2:"February",
             3:"March",4:"April",5:"May",
             6:"June",7:"Jnly",8:"August",
             9:"September",10:"October",
            11:"November",12:"Deceember"}
    return mn[m]

def pM(m,y):
    print('\t',gmn(m),' ',y)
    print('-------------------------------')
    print(' Sun Mon Tue Wed Thr Fri Sat ')
    #计算星期几
    sD=gD(m,y)
    for i in range(0,sD):
        print('    ',end="")
    #计算这个月有多少天
    sDm=gDm(m,y)
    for i in range(1,sDm+1):
        if i<10:
            tme='   %d'%i
        else:
            tme='  %d'%i
        print(tme,end="")
        if (i+sD)%7==0:
            print()

def gD(m,y):
    t=2
    for i in range(1980,y):
        if ly(i):
            t+=366
        else:
            t+=365
    for i in range(1,m):
        t+=gDm(i,y)
    return t%7

def gDm(m,y):
    lm1=[1,3,5,7,8,10,12]
    lm2=[4,6,9,11]
    if m in lm1:
        return 31
    if m in lm2:
        return 30
    if m==2:
        if ly(y):
            return 29
        else:
            return 28
    return 0

def ly(y):
    return (y%4==0 and y%100!=0) or y%400==0

year = int(input("请输入年份："))
month = int(input("请输入月份："))
pM(month,year)