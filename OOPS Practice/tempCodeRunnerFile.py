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
    def isvalidgrade(grade):
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

for i in range(len(student_details)):
    student_objects.append(Student(student_details[i]["name"],student_details[i]["age"],student_details[i]["grade"]))

print("Total students->",Student.total_student())
print(Student.isvalidgrade(student_objects[2].grade))