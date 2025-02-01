'''
Solution 4 and 5 
Inheritance
- Create a Vehicle class with attributes speed and fuel.
- Create a Car class that inherits from Vehicle and adds a new attribute seats.
'''

class Vehicle:
    def __init__(self,speed,fuel):
        self._speed = speed
        self._fuel = fuel
    
    def describe(self):
        print(f"This vehicle has a speed of {self._speed} km/h and runs on {self._fuel}.")

class Car(Vehicle):
    def __init__(self, speed, fuel,seats):
        self.__seats = seats
        super().__init__(speed, fuel)
    def describe(self):
        print(f"This car has a speed of {self._speed} km/h, runs on {self._fuel}, and has {self.__seats} seats.")

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self,speed):
        if isinstance(speed,int) and speed > 0:
            self._speed = speed
        else:
            print("Speed must be positive integer")
    
    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, fuel):
        if isinstance(fuel, str):
            self._fuel = fuel
        else:
            print("Fuel must be a string.")
    
    @property
    def seats(self):
        return self.__seats
    
    @seats.setter
    def seats(self,seats):
        if isinstance(seats,int) and seats > 0:
            self.__seats = seats
        else:
            print("Seat must be positive integer")

c1 = Car(speed=250,fuel="Petrol",seats=6)
print(f"Speed-> {c1.speed}\nFuel-> {c1.fuel}\nSeats-> {c1.seats}")
c1.describe()

'''
Static and Class Methods
************************
Implement a Student class with:
A class method to track the number of students.
A static method that validates a given grade (should be between 0-100).
'''
class Student:
    student_count = 0
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_count += 1
    
    @classmethod
    def total_student(cls):
        return cls.student_count
    
    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 100

    
student_details = [
    {"name": "Vivek Singh", "age": 24, "grade": 70},
    {"name": "Aisha Patel", "age": 22, "grade": 85},
    {"name": "David Lee", "age": 26, "grade": 68},
    {"name": "Maria Garcia", "age": 21, "grade": 92},
    {"name": "John Doe", "age": 25, "grade": 78}
]

print(len(student_details))

student_objects = []

for student in student_details:
    student_objects.append(Student(student["name"],student["age"],student["grade"]))

print("Total students->",Student.total_student())
print(Student.is_valid_grade(student_objects[2].grade))
    

