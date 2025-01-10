from Student import Student
import pickle

studs = [Student(101,"Barry Allen aka The Flash","Star City"),
         Student(102,"Clark Kent aka Superman","Metropolis"),
         Student(103, "Bruce Wayne aka Batman","Gotham"),
         Student(104, "Diana Prince aka Wonder Woman","Thymiscera"),
         Student(105, "Hal Jordan aka Green Lantern","Coast City")]
with open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\Students.data",'wb') as file:
    for class_object in studs:
        pickle.dump(class_object,file)    
with open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\Students.data",'rb') as file:
    for i in range(5):
        s = pickle.load(file)
        s.display()