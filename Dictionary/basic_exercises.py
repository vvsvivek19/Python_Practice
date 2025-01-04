#solution 1
car = [('brand','Tesla'),('model','X12'),('year',2023),('color','black')]
car_details = dict(car)
print(car_details)

#solution 2
print(car_details['model'])
car_details['color'] = 'white'
print(car_details['color'])
car_details['owner'] = 'Vivek'
print(car_details)

#solution 1 but extended
cars = [
    [('brand','Tesla'),('model','X12'),('year',2023),('color','black')],
    [('brand','Honda'),('model','Civic'),('year',2023),('color','red')],
    [('brand','Toyota'),('model','Innova'),('year',2023),('color','white')],
    [('brand','Jeep'),('model','Compass'),('year',2023),('color','red')]
    ]
car_details = {}
for x in range(len(cars)):
    car_details[x+1] = dict(cars[x])
print(car_details)

#solution 3
fruits = dict(mango=200,apple=100,banana = 150,guava=250,orange=160)
print(fruits)
for name in fruits.keys():
    print(name)
for price in fruits.values():
    print(price)
for name,price in fruits.items():
    print(name,"->",price)

#solution 4
genre = ['Fiction','Self Help','Science','Philosophy']
library = {}
library = library.fromkeys(genre)
#Using fromkeys() with [] creates a shared mutable list for all keys. When you append to one genre, 
#the same list is modified for all genres. This is a common pitfall.
print(library)
library = {key:[] for key in genre}
book1 = dict([('book name','Sapiens'),('Author','Yuval Noah Harrari'),('Published Year',2019)])
library['Science'].append(book1)
print(library)

#solution 5
from collections import Counter
word_counter = Counter("hippopotamus")
print(word_counter)

#solution 6
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
dict1.update(dict2)
print(dict1)

#solutions 7
values = dict1.values()
keys = dict1.keys() 
new_dict = dict(zip(list(values),list(keys)))
print(new_dict)

#solution 8
students = {"John": 85, "Emma": 92, "Liam": 78, "Sophia": 95, "Lucas": 68}
new_students = {}
for name,marks in students.items():
    if marks > 80:
        new_students[name] = marks
print(new_students)

#solution 9
fruits = dict(mango=200,apple=100,banana=150,guava=250,orange=160)
fruits = dict(sorted(fruits.items(),key=lambda item: item[1]))
print(fruits)

#solution 10
subjects = ['Math','Science','English']
subject_scores = {key:[] for key in subjects}
math = [90,99,87,67,89]
science = [87,88,77,99,78]
English = [90,54,67,89,98]
for x in range(5):
    subject_scores['Math'].append(math[x])
    subject_scores['Science'].append(science[x])
    subject_scores['English'].append(English[x])
print(subject_scores)
avg_math =sum(subject_scores['Math'])/len(subject_scores['Math'])
print("Avg score in math is ->", avg_math)

#solution 11
sales = {"Product A": 250, "Product B": 300, "Product C": 150, "Product D": 400}
maximum = max(sales.values())
for product,price in sales.items():
    if price == maximum:
        print("Product with maximum price ->", product)

#solution 12
#Update the salary of a specific employee.
#Find the average salary of employees.
#Add a new employee to the dictionary.
Employee_data = {
    1001: {
        'name': 'Vivek Singh',
        'age': 25,
        'department': 'Database',
        'salary': 20000
    },
    1002: {
        'name': 'Ananya Sharma',
        'age': 28,
        'department': 'Web Development',
        'salary': 25000
    },
    1003: {
        'name': 'Rohan Mehra',
        'age': 30,
        'department': 'Data Analysis',
        'salary': 30000
    },
    1004: {
        'name': 'Priya Verma',
        'age': 26,
        'department': 'Mobile Development',
        'salary': 28000
    },
    1005: {
        'name': 'Amit Khanna',
        'age': 29,
        'department': 'Cloud Services',
        'salary': 35000
    }
}
EID = int(input("Please Enter Employee ID: "))
print(f"Current salary of employee {EID} is {Employee_data[EID]['salary']}")
salary = int(input(f"Input new salary for the employee {EID}: "))
Employee_data[EID]['salary'] = salary
print("Update data for the employee: ")
print(Employee_data[EID])


salaries = []
total_employees = len(Employee_data)
for key in Employee_data.keys():
    salaries.append(Employee_data[key]['salary'])
salary_sum = sum(salaries)
average_salary = salary_sum/total_employees
print("Avg salary ->",average_salary)

print("Enter details of new employee: ")
EID = int(input("Enter the employee ID: "))
employee_details = ['name','age','department','salary']
new_employee_dict = {}
new_employee_dict = new_employee_dict.fromkeys(employee_details)
new_employee_dict['name'] = input("Enter name: ")
new_employee_dict['age'] = int(input("Enter age: "))
new_employee_dict['department'] = input("Enter department name: ")
new_employee_dict['salary'] = int(input("Enter salary: "))
Employee_data[EID] = new_employee_dict
print(Employee_data)
