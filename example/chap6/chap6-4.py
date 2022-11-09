import struct
def m():
    with open('d:\\pythontest\\test.bmp','rb') as f:
        a=struct.unpack("2s",f.read(2))
        b=struct.unpack("i",f.read(4))
        print(a[0].decode(),b[0])
m()
