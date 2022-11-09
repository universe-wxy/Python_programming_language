def is_c(uc):
    ac=ord(uc)
    if ac>=0 and ac<128:
        return False
    else:
        return True

def main():
    s=input("input sentence:")
    s1=""
    s2=""
    deal=1
    for u in s:
        if is_c(u):
            if deal==1:
                s2=s2+' '
                deal=0
            s1=s1+u
        else:
            if deal==0:
                deal=1
            s2=s2+u
    print(s1)
    print(s2)
main()
