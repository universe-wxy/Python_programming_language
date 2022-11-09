

# class Student:
#     def __init__(self, number, name, gender, room):
#         self.number = number
#         self.name = name
#         self.gender = gender
#         self.room = room
#
#     def __repr__(self):
#         return "学号:" + self.number + " " + "姓名:" + self.name + " " + "性别:" + self.gender + " " + "班级:" + self.room
import pickle
if __name__ == '__main__':
    n = int(input("请输入学员数量:"))
    stulist = []
    for i in range(n):
        number, name, gender, room = input("第%d个成员信息:" % (i + 1)).split(" ")
        number=int(number)
        stulist.append([number, name, gender, room])
    p = pickle.dumps(stulist)
    t = pickle.loads(p)
    nt = sorted(t, key=lambda s: s[0])
    for i in nt:
        print(i)
