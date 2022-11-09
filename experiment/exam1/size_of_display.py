import math

def anti_diagonal(length,rate):
    c=math.sqrt(rate[0]**2+rate[1]**2)
    a=length*rate[0]/c
    b=length*rate[1]/c
    return a,b


if __name__ == '__main__':
    rate=(16,9)
    length=float(input("请输入显示器尺寸（单位英寸）:"))
    a,b=anti_diagonal(length,rate)
    a,b=a*2.54,b*2.54
    print("显示器宽度为{}，显示器高度为{}（单位厘米）".format(a,b))