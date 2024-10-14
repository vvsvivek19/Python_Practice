num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")

#you can also use inbuilt max function to do this
# Use of ternary operator
#print(a if a >= b else b)

# python code to find maximum of two numbers using lambda functions
a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')