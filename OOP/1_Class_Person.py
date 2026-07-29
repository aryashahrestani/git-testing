class Person:
    """This is Class For Person"""
    name = "Fariborz"
    age = 42
    def func():
        print("This is a Method")


print(Person.age)
Person.func()
print(Person.__doc__)