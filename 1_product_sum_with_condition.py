#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1 = input("Enter the first number: ")
num1 = int(num1)
num2 = input("Enter the second number: ")
num2 = int(num2)

product = num1 * num2

if product <= 1000:
    print("Product of", num1, "and", num2, "is", product)
else:
    print("Sum of", num1, "and", num2, "is", num1 + num2)