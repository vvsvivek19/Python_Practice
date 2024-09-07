print("Program to print sum of n natural numbers.")
n = int(input("Enter the value of n: "))
natural_sum = 0
for i in range(1,n+1):
    natural_sum = natural_sum + i
print('Sum is',natural_sum)