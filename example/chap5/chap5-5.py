from math import *
def getDistance(x1, y1, x2, y2):
       return sqrt((x1-x2)**2+(y1-y2)**2)
def function():
    x=[1,-1,2,-2,4]
    y=[2,3,1.5,0,2]
    martix=[]
    max=0
    for i in range(len(x)):
      martix.append([])
      for j in range(len(x)):
          v=getDistance(x[i], y[i], x[j], y[j])
          martix[i].append(v)
          if max<martix[i][j]:
              max=martix[i][j]
    for i in range(len(x)):
        for j in range(len(x)):
            print("%5.2f"%martix[i][j],end="  ")
        print()
    print("max=%5.2f"%max)

if __name__ == '__main__':
    function()