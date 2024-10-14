P = int(input("Enter Principal: "))
R = int(input("Enter Rate: "))
T = int(input("Enter Time: "))
A = P * pow((1 + R/100),T)
CI = A - P
print(f"Compound Interest = {CI}")