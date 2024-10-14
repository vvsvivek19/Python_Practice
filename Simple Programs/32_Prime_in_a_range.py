start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
print(f"Prime numbers between {start} and {end} are: ")
for i in range(start,end+1):
    flag = 0
    for j in range(2,11):
        if i % j == 0:
            flag = 1
    if flag == 0:
            print(i)

