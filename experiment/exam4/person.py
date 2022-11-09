import sys
import datetime


class idException(Exception):
    pass
class nameException(Exception):
    pass
class dateException(Exception):
    pass

class person:
    id = int()
    name = str()
    date = int()

    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

    def setPer(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

    def show(self):
        print("{}   身份证号:{}     出生日期{}".format(self.name, self.id, self.date))


if __name__ == '__main__':
    print("开始输入人员信息:")
    Poslist=[]
    Perlist = []
    while 1:
        try:
            print()
            today=int(datetime.date.today().strftime('%Y%m%d'))
            id = int(input("请输入身份证号:"))
            if len(str(id)) != 18:
                raise idException
            name = input("请输入姓名:")
            if len(name) < 1 or len(name) > 16:
                raise nameException
            date = int(input("请输入出生日期:"))
            print(date)
            print(today)
            if date > today :
                raise dateException1
            tempPer = person(id, name, date)
            if today%10000-date%10000>=18:
                Poslist.append(len(Perlist))
            Perlist.append(tempPer)

        except idException:
            print("身份证号必须为18位，请重试")
        except nameException:
            print("姓名不低于1个汉字，高于16个汉字")
        except dateException:
            print("出生日期请输入八位数字且不能高于当前日期")
        confirm = input("是否继续输入")
        if confirm == "否":
            break
        elif confirm == "是":
            continue
        else:
            print("？？？")
            sys.exit(0)
    print("人员信息录入完毕")
    print("大于18岁的人有:")
    for i in Poslist:
        Perlist[i].show()