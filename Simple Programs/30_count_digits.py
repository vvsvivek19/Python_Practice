print("Program to count number of digits in a number.")
number = int(input("Enter a number: "))
orginal_num = number
count = 0
while number > 0:
    count += 1
    number = number // 10
print(f"Total digits in {orginal_num} are {count}")