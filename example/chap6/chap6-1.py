#利用文件读写函数写入字符串信息
try:
    with open('./test.txt','w')as f:
        f.write('山东\n威海\n')
        L=['文化西路2号','哈尔滨工业大学(威海)']
        f.writelines(L)#将列表L中的元素全部写入中介文件f中
        newL=[line + '\n'for line in L]#对于L列表中的每一行都再加一个换行
        f.writelines(newL)
        print("文件写入成功")
except:
    print("文件创建失败")