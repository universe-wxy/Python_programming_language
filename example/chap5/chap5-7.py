def gN(x):
    return x[1]
def function():
    txt=input('input text:')
    wordC={}
    for e in " !;.\t\n\"()-:#@":
        txt=txt.replace(e,',')
    L=txt.split(',')
    L.sort()
    while L[0].isdigit() or L[0]=='':
        del L[0]
    for e in L:
            if e in wordC:
                wordC[e]=wordC[e]+1
            else:
                wordC[e]=1
    print('按字典输出单词及次数（>2）:')
    words=list(wordC.keys())
    words.sort()
    for e in words:
            if wordC[e]>2:
                print(e,wordC[e])
    print('按字出现频率排序输出（>2）:')
    L1=list(wordC.items())
    L1.sort(key=gN,reverse=True)
    for i in range(len(L1)):
            if L1[i][1]>2:
                print(L1[i][0],L1[i][1])

if __name__ == '__main__':
    function()