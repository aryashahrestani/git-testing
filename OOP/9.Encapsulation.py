class Car:
    def __init__(self):
        self.__speed = None
        self.__color = None

    @property
    def speed(self):
        return self.__speed

    @ property
    def color(self):
        return self.__color

    @speed.setter
    def speed(self, value):
        if value >= 100 and value <= 200:
            self.__speed = value
        else:
            raise ValueError

    @color.setter
    def color(self, value):
        self.__color = value

    @speed.deleter
    def speed(self):
        del self.__speed

    @color.deleter
    def color(self):
        del self.__color

car1 = Car()
car1.speed = 150
car1.color = 'red'
# del car1.speed --> deleter
print(car1.speed)  # output: 200
print(car1.color) #output: red
