def func1(*args):
    for i in args:
        print(i, end=', ')
func1(1,2,3,60,80,90)

def calculation(num1,num2):
    Sum = num1 + num2
    Subtract = num1 - num2
    return Sum, Subtract

a,b = calculation(50,60)
print(a,b)

def show_employee(name,salary=9000):
    print('Name:',name)
    print("Salary:",salary)
show_employee("Ben", 12000)
show_employee("Jessa")

