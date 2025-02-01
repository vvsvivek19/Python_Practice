'''
Implement a Person class with private attributes (__name, __age) and public getter and setter methods to access them.
'''

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            print("Name must be a string")
     
    @age.setter
    def age(self,age):
        if isinstance(age,int) and age>0:
            self.__name = age
        else:
            print("Age must be a positive integer")

p1 = Person("Vivek Singh",20)
name = p1.name
print(name)
age = p1.age
print(age)
p1.name = "Vivek Singh chauhan"
name = p1.name
print(name)
p1.age = "asd"