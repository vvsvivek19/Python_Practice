num = int(input("Enter a Number: "))
fact = 1
if num == 0:
    print('Factorial is', fact)
else:
    for i  in range(1,num+1):
        fact = fact * i
    print('Factorial is', fact)