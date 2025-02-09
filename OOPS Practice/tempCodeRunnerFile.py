
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * (self.radius**2)

class Rectangle(Shape):
    def __init__(self,len,bre):
        self.length = len
        self.breadth = bre
    def area(self):
        return self.length * self.breadth

c1 = Circle(5.6)
print(c1.area())

r1 = Rectangle(6,3.7)
print(r1.area())
        