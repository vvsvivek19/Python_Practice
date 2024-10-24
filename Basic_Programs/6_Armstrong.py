num = input("Enter a number: ")
digits = len(num)
# print(digits)
num = int(num)
# print(type(num))
temp = num
sum = 0
while temp != 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10
print(sum)
if sum == num:
    print("Number is Armstrong")

#Another Approach
num = input("Enter a number: ")
sum = 0
digits = len(num)
for digit in num:
    sum = sum + int(digit)**digits
num = int(num)
if sum == num:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

#Another apprach with generators
def is_armstrong_number(number):
	return sum(int(digit)**len(str(number)) for digit in str(number)) == number


# Example usage:
num = 153
if is_armstrong_number(num):
	print(f"{num} is an Armstrong number")
else:
	print(f"{num} is not an Armstrong number")
