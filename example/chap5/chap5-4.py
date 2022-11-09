def type(s):
    if s[0:2]=="方块":
        return 4
    elif s[0:2]=="梅花":
        return 3
    elif s[0:2]=="红桃":
        return 2
    elif s[0:2]=="黑桃":
        return 1
    else:
        return 0
def value(s):
    if s[2:]=='A':
        return 14
    elif s[2:]=='K':
        return 13
    elif s[2:]=='Q':
        return 12
    elif s[2:]=='J':
        return 11
    else:
        return int(s[2:])

def remove(L):
    for e in L:
        for i in range(1,L.count(e)):
            L.remove(e)
    print("去掉重复的:",L)
def function():
    L=['梅花A','方块4','梅花2','方块4','红桃7','黑桃Q','红桃K','梅花9','方块9', '红桃5','梅花J','方块8','红桃5','黑桃3','黑桃10','黑桃3','红桃7','黑桃Q']
    #按花色排序
    L.sort(key=type)
    print("按花色排序:",L)
    i=0
    j=0
    p=["黑桃","红桃","梅花","方块"]
    L2=[]
    for k in range(4):
        i=j
        while j<len(L) and p[k] in L[j]:
            j=j+1
        s=L[i:j]
        s.sort(key=value, reverse=True)
        L2=L2+s
    L=L2
    print("按花色和顺序排序:",L)
    remove(L)

if __name__ == '__main__':
    function()
