import random

m=random.randint(1,9)
while 1:
    n=int(input("请输入一个1~9之间的数:\n"))
    if(n<1 or n>9):
        print("您输入的数字不符合要求")
        continue
    if(n<m):
        print("你猜的数字小了...")
    elif(n>m):
        print("你猜的数字大了...")
    else:
        print("恭喜，你猜对了！")
        break