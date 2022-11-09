from abc import ABCMeta,abstractmethod
class S(object):
    __metaclass__=ABCMeta
    def __init__(self):
        self.color='black'
    @abstractmethod
    def draw(self):pass

class Line(S):
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def draw(self):
        print('Draw line:(%d, %d, %d,%d)'%(self.x1,self.y1,self.x2,self.y2))

class C(S):
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def draw(self):
        print('Draw circle:(%d, %d, %d)'%(self.x,self.y,self.r))
def f():
    c=C(10,10,5)
    l=Line(5,5,15,15)
    lst=[]
    lst.append(c)
    lst.append(l)
    for k in range(len(lst)):
        lst[k].draw()
f()

