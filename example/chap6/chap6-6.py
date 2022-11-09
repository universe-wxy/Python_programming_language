# D:\\pythontest\\祝福你中华.txt
def readLRC(filename):
    with open(filename,'r') as f:
        res={}
        L=f.readline()
        while L!='':
            if(L[1:3].isdigit() and L[4:6].isdigit() and L[7:9].isdigit() and L[3]==':' and L[6]=='.'):
                t1=(int(L[1:3])*60+int(L[4:6]))*1000+int(L[7:9])*100
                res[t1]=L[10:].rstrip()
            L=f.readline()
        return res
def m():
    fname=input('输入MP3歌词文件名：')
    lrcD=readLRC(fname)
    for key in sorted(lrcD):
        print(key,lrcD[key])
m()
