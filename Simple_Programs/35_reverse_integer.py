num = int(input("Enter a number: "))
org_num = num
reverse = 0
while num > 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10
print(f'Reverse of number {org_num} is {reverse}')