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
    # The mode 'a+' allows appending and reading, but after appending, the 
    # file pointer is at the end. Use file.seek(0) to read from the beginning:
    file.seek(0)
    content = file.readlines()
    for item in content:
        print(item, end='')
finally:
    file.close()

#SOLUTION 9 - Except

try: 
    divisor = int(input("Enter a the divisor: "))
    # Using 'with open' for safer file handling
    with open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\data.txt",'r') as file:
        data = int(file.readline().strip()) # Strip extra spaces/newlines
    result = data/divisor
except FileNotFoundError as FNF:
    print("Error->",FNF)
except ZeroDivisionError as ZDE:
    print("Error: Cannot divide by zero:",ZDE)
except ValueError as VE:
    print("Error: Invalid input. Please ensure the divisor and file content are integers:",VE)
else:
    print(f"Result->{data}/{divisor} = {result}")


#SOLUTION 10 - password validator

class ShortPasswordError(Exception):
    def __init__(self, message = "Password cannot be less than 8 characters!"):
        self.message = message
        super().__init__(self.message)

class MissingNumberError(Exception):
    def __init__(self, message = "Please include atleast one digit in the password!"):
        self.message = message
        super().__init__(self.message)

class MissingSpecialCharacterError(Exception):
    def __init__(self, message = "Please include atleast one special character in the password!"):
        self.message = message
        super().__init__(self.message)

def check_digit(password):
    return any(item.isdigit() for item in password)

def check_special(password):
    for item in password:
        if not(item.isdigit() or item.isalpha()):
            return True
    return False
        

try:
    password = input("Please enter a password of 8 or more characters:").strip()
    if(len(password) < 8):
        raise ShortPasswordError
    if(check_digit(password)):
        pass
    else:
        raise MissingNumberError
    if(check_special(password)):
        pass
    else:
        raise MissingSpecialCharacterError
except ShortPasswordError as msg:
    print(msg)
except MissingNumberError as msg:
    print(msg)
except MissingSpecialCharacterError as msg:
    print(msg)
else:
    print("Enter password is acceptable!!!")

#solution 11 - Logging errors

from datetime import datetime

log_file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\logs.txt"

try:
    num1 = None
    num2 = None
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError as msg:
    log_entry = f"[{datetime.now()}] ValueError: {msg} | Inputs: num1 = {num1}, num2 = {num2}\n"
    with open(log_file_path,'a+') as file:
        file.write(log_entry)
    print("ValueError logged successfully")
except ZeroDivisionError as msg:
    log_entry = f"[{datetime.now()}] ZeroDivisionError: {msg} | inputs: num1 = {num1}, num2 = {num2}\n"
    with open(log_file_path,'a+') as file:
        file.write(log_entry)
    print("ZeroDivisionError logged successfully")
except Exception as msg:
    log_entry = f"[{datetime.now()}] UnexpectedError: {msg}\n"
    with open(log_file_path,'a+') as file:
        file.write(log_entry)
    print("Unexpected Error logged successfully")
    
#Solution 12 - Reraising exception:
'''
Key Points
************
Why Re-raise?
-------------
Sometimes, you may need to handle an exception partially (e.g., perform cleanup) but still 
propagate it for further processing, logging, or user notification.

Use Case:
    -Resource management (e.g., closing files, releasing database connections).
    -Logging the error locally and propagating it globally.
finally Block:
    -Even after re-raising an exception, the finally block is executed, making it ideal for 
    tasks that must always be performed (e.g., resource cleanup).
'''
def process_file(file_path):
    try:
        # Step 1: Open the file
        file = open(file_path, 'r')
        
        # Step 2: Perform some operation (e.g., read a line)
        line = file.readline()
        print("First line of the file:", line)
        
        # Step 3: Introduce an exception
        result = 10 / 0  # Deliberately causing a ZeroDivisionError
        
    except ZeroDivisionError as zde:
        # Step 4: Handle the exception locally
        print("Caught an exception:", zde)
        print("Performing cleanup (e.g., closing the file).")
        file.close()  # Cleanup
        
        # Step 5: Re-raise the exception
        raise
    finally:
        print("This block always executes (even after re-raising).")

# Global Exception Handling
log_file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\logs.txt"
try:
    process_file(log_file_path)
except Exception as e:
    print("Global handler caught the exception:", e)

'''
In the above code, while re-raising the exception using raise, the exception's type 
(like ZeroDivisionError) is not explicitly specified because:
    -raise without an argument propagates the current exception: When you use raise alone in an 
    except block, it automatically re-raises the exception that is currently being handled. 
    The Python interpreter knows the context of the exception because it is inside the except block.
    - Writing raise ZeroDivisionError explicitly in the except block creates a new instance of the 
    ZeroDivisionError, losing the original traceback and context of where the exception occurred. 
    This makes debugging harder because the original location of the error is overwritten.
    -No need to specify the exception again: Specifying the exception type again would be redundant. 
    You already caught the exception in the except block (in this case, ZeroDivisionError as zde), 
    so Python assumes you want to re-raise the same exception.
'''
    