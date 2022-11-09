class C:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def __del__(self):
        print('bye')

class T(C):
    def __init__(self,id,name,age,Thno,dept,sal):
        super(T,self).__init__(id,name,age)
        self.Thno=Thno
        self.dept=dept
        self.sal=sal

class S(C):
    def __init__(self,id,name,age,stdno,grade,score):
        super(S,self).__init__(id,name,age)
        self.stdno=stdno
        self.grade=grade
        self.score=score
if __name__=='__main__':
    c=C('01','张三疯',65)
    print(c.id,c.name,c.age)
    del c
    s=S('02','张无忌',18,'160400101',1,95)
    print(s.id,s.name,s.age,s.stdno,s.grade,s.score)
    del s
    t=T('01','张cuishan',40,'0101022','computer',6000)
    print(t.id,t.name,t.age,t.Thno,t.dept,t.sal)
