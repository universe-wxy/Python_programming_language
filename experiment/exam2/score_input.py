if __name__ == '__main__':
    num = int(input("请输入学生个数:"))
    for i in range(num):
        try:
            grade = int(input("请输入学生成绩:"))
            assert 0 <= grade <= 100
            print("学生成绩为{}".format(grade))
            print("成绩评价为：", end="")
            if grade >= 90:
                print("A.优秀")
            elif grade >= 80:
                print("B.良好")
            elif grade >= 70:
                print("C.合格")
            elif grade >= 60:
                print("D.及格")
            else:
                print("E.不及格")
        except AssertionError:
            print("分数不合理")
        except IOError:
            print("输入操作异常")