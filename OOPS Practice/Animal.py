import random
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
        print(f"{self.name} wants to play")

d = Dog("Bolt", "German Sheperd")
d.make_sound()

a = Animal("Kal El", "Kryptonian")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
    def cat_mood(self,choice = random.randint(1,3)):
        if choice == 1:
            print(f"{self.name} wants to play")
        if choice == 2:
            print(f"{self.name} is hungry")
        if choice == 3:
            print(f"{self.name} is angry, stay away from it.")

c = Cat("Garfield","Persian")
c.cat_mood()

'''
Learning:
1. Using Animal.__init__(self, ...)
When you explicitly call the parent class's constructor (Animal.__init__(self, ...)) inside the child class, you are directly invoking the method as a regular function. Since self represents the instance on which the method is invoked, you must pass self explicitly when calling it this way.
Example: Animal.__init__(self, name, species="Dog")
Here, you're calling Animal.__init__ as if it were an independent function. Without explicitly passing self, the method would not know which instance it should initialize.

2. Using super().__init__(...)
When you use super().__init__(...), Python automatically manages the self parameter for you. The super() function returns a proxy object that automatically forwards the method call to the parent class. You do not need to explicitly pass self because super() is context-aware and knows that it's being called from within a method of the child class.
Example: super().__init__(name, species="Dog")
Here, super() knows that self refers to the current instance of the Dog class, so it passes self implicitly to the __init__ method of the Animal class.

Best Practice
It is recommended to use super() instead of directly calling the parent class's methods. It makes your code cleaner, supports multiple inheritance scenarios, and avoids potential issues with MRO.
'''