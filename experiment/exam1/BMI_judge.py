def cal_BMI(height,weight):
    return weight/(height**2)

if __name__ == '__main__':
    weight=float(input("请输入体重："))
    height=float(input("请输入身高："))
    BMI=cal_BMI(height,weight)
    print("您的BMI值为：%f"%BMI)
    if BMI>30:
        print("您的BMI值在肥胖区间，注意身材已经刻不容缓了！")
    elif BMI>25:
        print("您的BMI在超重区间，建议控制饮食")
    elif BMI>20:
        print("您的BMI在正常区间，请继续保持")
    else:
        print("您的BMI在偏廋区间，请您多吃点")
