if __name__ == '__main__':
    n=int(input("请输入落地的次数"))
    height=100
    cnt=-100
    for i in range(n):
        cnt+=2*height
        height/=2
    print("在第{}次落地时，一共经过{}米".format(n,cnt))