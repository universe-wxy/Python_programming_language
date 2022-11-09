import math
import circle


class cylinder(circle.circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.__radius = radius
        self.__height = height

    def setR(self, R):
        self.__radius = R

    def setH(self, H):
        self.__height = H

    def getR(self):
        return self.__radius

    def getH(self):
        return self.__height

    def getV(self):
        return math.pi * (self.__radius ** 2) * self.__height

    def show(self):
        print("圆柱的半径和高分别为{},{}".format(self.__radius, self.__height))
        print("圆柱的体积为{}".format(self.getV()))
