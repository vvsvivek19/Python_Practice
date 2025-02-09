'''
Polymorphism
- Implement two classes, Dog and Cat, each with a make_sound() method.
- Create a function animal_sound() that accepts an object and calls its make_sound() method.
'''
class Dog:
    def make_sound(self):
        print("Dog barks")

class Cat:
    def make_sound(self):
        print("Cat Meows")

def animal_sound(animal):
    animal.make_sound()

d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)

'''
Magic (Dunder) Methods
Implement a Book class with __str__ and __len__ methods.
- __str__ should return the book’s title, and __len__ should return the number of pages.
'''

class Book:
    def __init__(self,name,no_of_pages):
        self.name = name
        self.nop = no_of_pages
    
    def __str__(self):
        return self.name
    
    def __len__(self):
        return self.nop

book1 = Book("Sapiens",400)
print(book1)
print(len(book1))

'''
Composition
- Create an Engine class with an attribute horsepower.
- Create a Car class that has an Engine object as a property.
'''

class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self,model,engine,price):
        self.model = model
        self.car_horsepower = engine.horsepower
        self.price = price
    def print_details(self):
        print(f"Name: {self.model}\nHorsepower: {self.car_horsepower}\nPrice: {self.price}")

e1 = Engine(1000)
c1 = Car("Mclaren F1",e1,10000000)
c1.print_details()

'''
Abstract Classes and Interfaces (ABC Module)
- Define an abstract class Shape with an abstract method area().
- Implement Circle and Rectangle classes that inherit from Shape and provide implementations for area().
'''

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
print(f"Circle Area: {c1.area():.2f}")

r1 = Rectangle(6,3.7)
print(f"Rectangle Area: {r1.area():.2f}")
        