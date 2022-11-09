def numberOfSoldier(a,b,c):
    #CRT
    sTotal=(70*a+21*b+15*c)%105
    return sTotal

if __name__ == '__main__':
    a,b,c,=input("请输入三种排法的余量:").split()
    a=int(a)
    b=int(b)
    c=int(c)
    sTotal=numberOfSoldier(a,b,c)
    print("最少拥有士兵的数量为{}".format(sTotal))
