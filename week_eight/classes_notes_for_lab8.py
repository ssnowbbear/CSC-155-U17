# EX 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(3, 5)
print('x',p.x, 'y',p.y)

# 'class' denotes a class declaration
# class name in example is point

# def__init__ is a constructor. constructs an object.
# EVERY CLASS CONSTRUCTOR IS NAMED __init__

#self if a reference to our object, can assign attributes to it.
#we assign x and y that are passed in to attributes x and y of self

#p is an instantiation of a point. instantiation aka an object
#p = Point(3,5) calls the __init__ function. in the case of constructors
#'self' is reference an object created by python for us. 3 is passed into x
# 5 is passed into y, self is returned and assigned to p

# classes allow named access to data members. p.x would give 3 for example
# tuples need to be indexed or unpacked.

t = (3,5)
print('x', t[0]) #indexing

x, y = t
print('x', x) #unpacking

# method = function that is defined inside of a 'class' 
# a 'method' is a type of function
# call a 'method' by using an instance of the class, given as the first argument
# parameter is almost always named 'self', its a convention everyone uses.

# Distance method:

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y 
    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**.5
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
p = Point(0, 0)
q = Point(1, 1)

p.distance(q)

print(p.distance(q))
print(f'[{p}, {q}]')

# ^^^invokes method 'distance'. python becomes wizard(magic),
# then self and p refer to the same point. p is passed in as self
# 'q' (an argument) is passed in to 'other' (a parameter).
# what is actually passed in is a value of the 
# memory address of our point object.
# need to print it to see the distance

# by default, python will print the memory location rather
# than the value of its contents when printing objects

# # print(p) # <- memory location print

# an object is an instance of a class, in this case, the 'point' class
# 0x indicates hexadecimal number(base 16, meaning there are
# 16 digits used to represent a number)

# can change the print behavior by defining __str__ or by using __repr__
# __repr__ is better because it works on list of our objects

# MORE COMPLEX OBJECTS

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def __repr__(self):
        return f'Center: {self.center}, Radius = {self.radius}'
    
p = Point (1,1)
c = Circle (p, 5)
d = Circle(Point(2, 3), 7)

print('c', c)
print('d center x value:', d.center.x)

# DUCK TYPING 
# > Python is duck typing language. "if it looks like a duck,
# then it is a duck". Basically objects either have properties or not.
# Duck typing refers to the idea that the suitability of an object
# for a particular purpose is determined by the presence of 
# certain methods and properties, rather than the actual type
# of the object being a specific class

class Cat:
    def speak(self):
        print('Meowza')

class Dog:
    def speak(self):
        print('Woofy')

tabby = Cat()
tiger = Cat()

tabby.speak() # <- works for 'tabby' instance of 'class Cat'
tiger.speak() # <- works for 'tiger' instance of 'class Cat' 
# ^^^ when self is parameter
Cat.speak() # <- have to use when self not in 'class Cat'
animals = [Cat(), Dog()]
for a in animals:
    a.speak()