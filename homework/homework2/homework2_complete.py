cnt=0
for x in range(1,10000):
    cnt=0
    for i in range(1,x):
        if(x%i==0):
            cnt+=i
    if(cnt==x):
        print(x)