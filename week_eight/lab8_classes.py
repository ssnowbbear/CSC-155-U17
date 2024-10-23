# > 1) Make a rectangle
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self): # > 2) Add an area function
        return self.width * self.height
    def __repr__(self):
        return f'Width: {self.width} \nHeight: {self.height}'

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y 
    # def distance(self, other):
    #     return ((self.x-other.x)**2 + (self.y-other.y)**2)**.5
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2) # > 3) Add area to circle
    def __repr__(self):
        return f'Center: {self.center}, Radius = {self.radius}'

# RECTANGLE STUFF-----------------------
rect_dimen = Rectangle (4, 10)
rect_area = rect_dimen.area()

print(rect_dimen)
print(f'Area of the rectangle: {rect_area}') # > Part of problem (2)
# RECTANGLE STUFF-----------------------

# CIRCLE STUFF---------------------------
cp = Point (1, 2)
c_cr = Circle(cp, 4)

circ_area = c_cr.area() 

print(f'Area of the circle: {circ_area:.2f}') # > Part of problem (3)
# CIRCLE STUFF---------------------------

# > 4) List of Circle and Rectangle
objects = [Rectangle(2, 7), Circle(Point(2, 1), 9), rect_dimen, c_cr]

# > 5) Find average area in list
total_area = 0 
for object in objects:
    total_area += object.area()
# print(total_area) # check to see that area function was working

avg_area = total_area/len(objects)
print(f'Average area: {avg_area:.2f}')

# > 6) Largest shape in list
all_area = []
for object in objects:
    all_area.append(object.area())

largest_area = max(all_area)

for object in objects:
    if object.area() == largest_area:
        print(f'The largest shape is: {object}')

# > 7) Sort list by area
sorted_objects = [x for _, x in sorted(zip(all_area, objects))]
# print(sorted_objects) # make sure sort function worked properly
# print(f'\nThe sorted list of shapes: {sorted_objects}') 
# ^^^wanted to see what looked better

print("\nThe sorted list of shapes:")
for object in sorted_objects:
    print(f'\n{object}')