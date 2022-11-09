def SDrepCount(txt,word,repword):
    cnt=txt.count(word)
    return txt.replace(word,repword),cnt

if __name__ == '__main__':
    txt=input("请输入一段文本")
    word=input("请输入要被替换的词汇")
    repword=input("请输入替换的词汇")
    str,cnt=SDrepCount(txt,word,repword)
    print("替换后的文本内容为{}".format(str))
    print("替换的次数为{}".format(cnt))