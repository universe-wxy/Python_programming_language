if __name__ == '__main__':
    print("下面录入用户")
    num=int(input("请输入用户个数"))
    dict={}
    for i in range(num):
        user,passwd=input("请输入账号密码").split()
        dict.update({user:passwd})

    print()
    print("下面进行登录")
    for i in range(3):
        name,pd=input("请输入用户名密码").split()
        if dict[name]==pd:
            print("登录成功")
            break
        else:
            print("账号或密码错误")