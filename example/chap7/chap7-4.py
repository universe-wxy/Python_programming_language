class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,v):
        return self.x+v.x,self.y+v.y
    def __sub__(self,v):
        return self.x-v.x,self.y-v.y
    def __mul__(self,v):
        return self.x*v.x,self.y*v.y
    def f():
        v1=Vector2(1,2)
        v2=Vector2(3,4)
        print(v1+v2)
        print(v2*v1)

Vector2.f()