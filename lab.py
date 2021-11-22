class Car:
    def __init__(self, __year, __make, __model, __speed):
        self.__year = __year
        self.__make = __make
        self.__model = __model
        self.__speed = __speed

    def setYear(self, __year):
        self.__year = __year

    def getYear(self):
        return self.__year

    def setMake(self, __make):
        self.__make = __make

    def getMake(self):
        return self.__make

    def setModel(self, __model):
        self.__model = __model

    def getModel(self):
        return self.__model

    def setSpeed(self, __speed):
        self.__speed = __speed

    def getSpeed(self):
        return self.__speed

    def accelerate(self):
        if (self.__speed > 120):
            print("Speed exceed 120")
        else:
            self.__speed += 5

    def Break(self, __speed):
        if (self.__speed < 0):
            print("Speed is below O")
        else:
            self.__speed -= 5

    def getSpeed(self, __speed):
        return self.__speed


vehicle = Car(2000, 'Ford', 'C50', 5)
# Let's call the accelerate method five times
vehicle.accelerate()
print("The speed ", vehicle.getSpeed)
vehicle.accelerate()
vehicle.accelerate()
vehicle.accelerate()
vehicle.accelerate()
