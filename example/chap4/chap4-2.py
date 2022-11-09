def calc_grade(math, english, chinese):
    Sum=math+english+chinese
    Avg=float(Sum/3)
    return Sum,Avg

math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
chinese = int(input("请输入语文成绩："))
a,b=calc_grade(math,english,chinese)
print("总成绩：",a," ","平均成绩：",b)