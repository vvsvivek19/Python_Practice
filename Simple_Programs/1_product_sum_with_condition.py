#Given two integer numbers, return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

def prod_sum(num1,num2):
    if (num1 * num2) >=1000:
        return num1 * num2
    else:
        return num1 + num2
    
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("result is", prod_sum(num1,num2))
