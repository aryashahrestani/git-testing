class Math():
    """Math class docstring"""
    def __init__(self, number1,number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2

    def multi(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 / self.number2
obj1 = Math(6,2)
print(obj1.sum())
print(obj1.sub())
print(obj1.multi())
print(obj1.div())
obj2 = Math(12,2)
print(obj2.sum())
print(obj2.sub())
print(obj2.multi())
print(obj2.div())