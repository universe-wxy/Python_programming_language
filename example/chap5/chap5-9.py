def fibonacci():
    a=b=1
    yield(a)
    yield(b)
    while True:
        a,b=b,a+b
        yield(b)
def m():
    for num in fibonacci():
        if num>100:
            break
        print(num, end=' ')
m()