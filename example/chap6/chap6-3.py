import struct
def m():
    with open('d:\\pythontest\\grade.bin','wb') as f:
        s1='张三疯'.encode('utf-8')
        s2='机械无忌'.encode('utf-8')
        byte=struct.pack("!10s12si",s1,s2,128)
        f.write(byte)
    with open('d:\\pythontest\\grade.bin','rb') as f:
        a,b,c=struct.unpack("!10s12si",f.read(12+18+4))
    print(a.decode("utf-8",'ignore'),b.decode("utf-8", 'ignore'),c)
m()
