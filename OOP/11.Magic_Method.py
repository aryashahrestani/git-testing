class Test():
    """docstring for Test"""
    def __init__(self):
        self.lst = [13,18,20]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        return self.lst[i]

    def __setitem__(self, i, v):
        self.lst[i] = v
obj1 = Test()
print(obj1) # [13, 18, 20] --> __str__
print(len(obj1)) # 3 --> __len__
print(obj1[1]) # 18 --> __getitem__
obj1[1] = 22
print(obj1[1]) # 22 --> __setitem__