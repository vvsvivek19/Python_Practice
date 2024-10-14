my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l = len(my_list)
print("Program to print elements at odd index: ")
for i in range(l):
    if i == 0:
        continue
    elif i % 2 != 0:
        print(my_list[i], end=' ')