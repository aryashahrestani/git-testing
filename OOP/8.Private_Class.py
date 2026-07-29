class Test():
    """docstring for Test"""
    __privateVar = 2 # private variable
    def __privateMethod(self): # private Method
        print(1)

    def g(self):
        return (self.__privateMethod())

obj1 = Test() #
obj1.g() # output: 1
obj1.__privateMethod() # AttributeError