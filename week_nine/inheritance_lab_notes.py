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
class Parent(Grandparent): #inherits from Grandparent
    def __init__(self):
        super().__init__()
class Child(Parent): #inherits from Parent
    def __init__(self):
        super().__init__()

c = Child()
# print(c.x) # prints 3 from Grandparent

# Inheritance if normally used for 'x' 'is a type of' 'y' relationships
# >(in online lab diagram) an arrow pointing from one object to another
# means 'is a type of,' for example Bluejay 'is a type of' Bird

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# GAME Example: (Check notebook/phone/lab for diagram)
# An arrow from Hobgoblin -> Goblin means Hobgoblin 'is a type of'
# Goblin. Arrow also = 'inherits from' as in Hobgoblin will inherit
# all the code from Goblin. This is useful because the game could
# have goblins that behave 'goblin-y' but maybe they are stronger
# and look tougher and they drop better loot. 
# So we reuse as much of the code as possible using inheritance
# (OF INTEREST!)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Overriding (cont...)