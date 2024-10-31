# Inheritance = a class declared as a subclass of another class.
# > The subclass(child) receives all the code of the super(parent) class.
# > Two goals of inheritance are promoting code reusability &
# > preventing repeated code

# >>Example 1<<
class Parent():
    def __init__(self):
        pass
class Child(Parent):
    def __init__(self):
        super().__init__() #inherits from parent

# A subclass(child) can be the parent of another class

# >>Example 2<<
class Grandparent():
    def __init__(self):
        self.x = 3
class Parent(Grandparent):
    def __init__(self):
        super().__init__()
class Child(Parent):
    def __init__(self):
        super().__init__()

c = Child()
print(c.x) # prints 3 from Grandparent