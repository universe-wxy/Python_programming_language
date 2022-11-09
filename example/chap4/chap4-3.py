def f1():
    x=y=2
    def f2():
        y=3
        print('f2:x=',x)
        print('f2:y=',y)
    f2()
    print('f1:x=',x)
    print('f2:y=',y)

f1()