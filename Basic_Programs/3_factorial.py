#normal menthod, it works
num = int(input("Enter a number: "))
fact = 1
i = 1
while(i<=num):
    fact = fact * i
    i += 1
print(f"Factorial of {num} is {fact}")

#recursive approach
def fact(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * fact(n-1)
num = int(input("Enter a number: "))
factorial = fact(num)
print(f"Factorial of {num} is {factorial}")

#Find Factorials quickly using One liner (Using Ternary Operator)
def fact(n):
    return 1 if(n==1 or n==0) else n * fact(n-1)
num = int(input("Enter a number: "))
factorial = fact(num)
print(f"Factorial of {num} is {factorial}")

#You can directly use the factorial function from the math module if you want