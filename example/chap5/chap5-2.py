def substr():
    s1=input('输入子串1：')
    s2=input('输入子串2：')
    r=""
    m=0
    for i in range(0,len(s2)):
        for j in range(i+1,len(s2)+1):
            if s2[i:j] in s1 and m<j-i:
                r=s2[i:j]
                m=j-i
    print("最长公共的子串：",r)
substr()
