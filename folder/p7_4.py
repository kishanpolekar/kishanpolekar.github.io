class Fan:
    def __init__(self):
        self.SLOW=1
        self.MEDIUM=2
        self.FAST=3
        self.__speed=self.SLOW
        self.__on=False
        self.__radius=5.0
        self.__color="Blue"

    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed=speed

    def getOn(self):
        return self.__on
    def setOn(self, on):
        self.__on=on

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius=radius

    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color=color
