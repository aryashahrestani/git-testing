class Para:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def paraArea(self):
        print(f'Parallelogram Area = x*h --> {self.x} * {self.y} = {self.x * self.y}')

class Rec(Para):
    def __init__(self,x,y):
        Para.__init__(self,x,y)
        self.y = y
    def RecArea(self):
        print(f'Rectangle Area = x*y --> {self.x} * {self.y} = {self.x*self.y}')
class Squ(Rec):
    def __init__(self,x, y = None):
        Rec.__init__(self,x, y = None)

    def squArea(self):
        print(f'Square Area = x*x --> {self.x} * {self.x} = {self.x * self.x}')

squ1 = Squ(5)
squ1.squArea() # Square Area = x*x --> 5 * 5 = 25
rec1 = Rec(2,5)
rec1.RecArea()
para1 = Para(3,6)
para1.paraArea()
