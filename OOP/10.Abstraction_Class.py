from abc import ABC,abstractclassmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def eat(self):
        pass
class Dog(Animal):
    def eat(self):
        print('Meat')

class Sheep(Animal):
    def eat(self):
        print('Hay')

dog = Dog('Mack')
cat = Sheep('Missy')

dog.eat() # output: Meat
cat.eat() #output: Hay