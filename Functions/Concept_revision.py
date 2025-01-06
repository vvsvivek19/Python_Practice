def calculate_area(length, width):
    area = length * width
    return area
print('Positional Arguments ->',calculate_area(10,5))
print('Keyword Arguments ->',calculate_area(length=15,width=5))

def greet(name,greeting="Hello"):
    print(greeting, name)

greet("Vivek", "Kese ho")
greet("Vivek")

def calculate_sum(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print(calculate_sum(2,4,6,8,9,18,90,34,67,89,90,100,899,873))

def find_max(*numbers):
    return max(numbers)
num_list = [3,6,9,17,43,23,67]
print(find_max(*num_list))

def min_max_avg(numbers):
    mininum = min(numbers)
    maximum = max(numbers)
    avg = sum(numbers)/len(numbers)
    return mininum, maximum, avg

minimum, maximum, avg = min_max_avg(num_list)
print("minimum ->", minimum)
print("maximum ->", maximum)
print("minimum ->", avg)

def print_employee_details(**kwargs):
    print(kwargs)
print_employee_details(name="John", age=30, department="HR")

def multiply_by_two(x):
    return x*2
def apply_function(func, value):
    print(func(value))
apply_function(multiply_by_two, 6)

def make_multiplier(n):
    def multiplier(m):
        print(n * m)
    return multiplier             
m = make_multiplier(3)
print(m(5))

import logging
logging.basicConfig(level=logging.INFO)
def log_calling_function(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args,**kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper
@log_calling_function
def add(a,b):
    return a + b

add(5,6)

square = lambda x: x**2
print(square(10))