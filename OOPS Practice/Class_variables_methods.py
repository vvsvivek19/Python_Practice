class Student:
    #class variable
    school_name = "Hogwarts Academy of Magic"
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #class method
    @classmethod
    def change_school_name(cls,new_school_name):
        cls.school_name = new_school_name
    
    #instance method
    def show_details(self):
        print("Below are details of the student")
        print("Name->",self.name)
        print("Age->",self.age)
        print("School->",Student.school_name) #If I used self then it would create a new instance variable of the same name
        print("***********************************")

student_1 = Student("Harry Potter", 14)
student_2 = Student("Hermione Granger",14)
student_1.show_details()
student_2.show_details()
student_2.school_name = "Russian Academy of Magic"
student_1.show_details()
student_2.show_details()