import math

class circle:
    def __init__(self,radius):
        self.__radius=radius

    def setR(self,radius):
        self.__radius=radius

    def getR(self):
        return self.__radius

    def getS(self):
        return math.pi*(self.__radius**2)

    def show(self):
        print("圆的半径为{}".format(self.__radius))
        print("圆的面积为{}".format(self.getS()))
