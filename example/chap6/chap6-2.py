try:
    with open("./test.txt",'r') as f:
        s1=f.read(2)
        print(s1)
        print(f.tell())
        f.seek(6,0)
        s1=f.read(4)
        print(s1)
except FileNotFoundError:
    print('文件创建未发现')
try:
    with open("./test.txt",'r') as f:
        i=1
        for line in f:
            print('第',str(i),'行：',line, end="")
            i=i+1
except FileNotFoundError:
    print('文件创建未发现')
