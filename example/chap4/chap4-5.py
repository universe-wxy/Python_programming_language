def Hanoi(n,ch1,ch2,ch3):
    if n==1:
        print(ch1,'->',ch3)
    else:
        Hanoi(n-1,ch1,ch3,ch2)
        print(ch1,'->',ch3)
        Hanoi(n-1,ch2,ch1,ch3)

Hanoi(3,'A','B','C')