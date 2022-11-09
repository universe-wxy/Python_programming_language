class compl:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self, c):
        return compl(self.r + c.r, self.i + c.i)

    def __mul__(self, c):
        return compl(self.r * c.r -
                     self.i * c.i, self.r * c.i + c.r * self.i)
    def f():
        c1=compl(3,4)
        c2=compl(6,-7)
        c3=c1+c2
        c4=c1*c2
        c4.show()
        (c1+c2).show()

    def show(self):
        print(self.r, "+", self.i, 'j')

compl.f()