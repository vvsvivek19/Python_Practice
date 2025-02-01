'''
Create a Class and Object
    - Define a Car class with attributes like brand, model, and year.
    - Create an instance of the class and print its attributes.
'''
class Car:
    def __init__(self,brand,model,year):
        self.__brand = brand
        self.__model = model
        self.__year = year
    def __str__(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}"
    def print_details(self):
        print("Details of car")
        print("********************")
        print("Brand->",self._brand)
        print("Model->",self._model)
        print(f"Year-> {self._year}\n")
        
        
car1 = Car("Mercedes","SLS 100",2025)
car2 = Car("Hundai","Venue",2024)
car1.print_details()
car2.print_details()

'''
Create a BankAccount class with a class variable bank_name and instance variables account_holder 
and balance.
'''

class BankAccount:
    bank_name = "World Bank"
    account_num = 1001
    def __init__(self,account_holder,balance):
        self._account_holder = account_holder
        self._account_number = BankAccount.account_num
        BankAccount.account_num += 1
        self._balance = balance
    def print_details(self):
        print("Account Holder's details: ")
        print("*****************************")
        print("Account Number->",self._account_number)
        print("Name->",self._account_holder)
        print(f"Balance-> {self._balance}")

acc1 = BankAccount("Vivek Singh",10000)
acc1.print_details()
acc2 = BankAccount("Bittu Singh",10000)
acc2.print_details()
        
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

            