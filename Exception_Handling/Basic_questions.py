#SOLUTION 1

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    result = a / b
except ZeroDivisionError as mgs:
    print(f"{mgs}:Can't divide a number by zero")
else:
    print("Result:",result)
    
#SOLUTION 2

try: 
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
except ValueError as msg:
    print(f"{msg}:Please enter a integer and nothing else")
else:
    sum = num1 + num2
    print("Result:",sum)

#SOLUTION 3

try:
    file = open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\sample.txt",'r')
    #There is file named sample.txt in the above mentioned path with content
    #This is sample text to test exception handling of opening a file
except FileNotFoundError as msg:
    print(f"{msg}: File not found or it is inaccessible")
else:
    content = file.read()
    print("Content of file->",content)
finally:
    file.close()

#SOLUTION 4

list1 = [1,2,3,5,6,7,8]
list2 = [1,2,3,5,6,7,8,'AirBnb']
try:
    sum1 = 0
    sum2 = 0
    for item in list1:
        sum1 = sum1 + item
    for item in list2:
        sum2 = sum2 + item
except TypeError as msg:
    print(msg)
else:
    print("Sum of list 1->",sum1)
    print("Sum of list 2->",sum2)

#SOLUTION 5

class NegativeValueError(Exception):
    def __init__(self, message = "Input value cannot be negative"):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeValueError
except (NegativeValueError,ValueError) as msg:
    print(msg)
else:
    print("Successfully enter a positive integer")

#SOLUTION 6

try:
    a = int(input("Enter a number: "))
    try: 
        b = int(input("Enter another number: "))
        try: 
            result = a / b
        except ZeroDivisionError as mgs:
            print(f"{mgs}:Can't divide a number by zero")
        else:
            print("Result:",result)
    except:
        print(f"{msg}:Please enter a integer and nothing else")
    else:
        pass
except ValueError as msg:
    print(f"{msg}:Please enter a integer and nothing else")
else:
    pass

#SOLUTION 8

try:
    file = open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\sample.txt",'a+')
    str1 = '\nPython is easy\nIt is simple\nEverything is an object\n'
    file.write(str1)
    #There is file named sample.txt in the above mentioned path with content
    #This is sample text to test exception handling of opening a file
except FileNotFoundError as msg:
    print(f"{msg}: File not found or it is inaccessible")
else:
    content = file.readlines()
    print(content)
    # for item in content:
    #     print(item, end='')
finally:
    file.close()
