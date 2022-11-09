def SDsearch(txt,word):
    temp=txt.find(word)
    pos=[]
    while temp!=-1:
        pos.append(temp)
        temp=txt.find(word,temp+1)
    return pos

if __name__ == '__main__':
    txt=input("请输入一段文本").strip()
    word=input("请输入寻找的词汇").strip()
    list=SDsearch(txt,word)
    print(list)