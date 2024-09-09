numbers = [i for i in range(4,30) if i % 2 == 0]
print(numbers)

def largest(list1):
    largest_num = 0
    for i in list1:
        if i > largest_num:
            largest_num = i
    return largest_num
x = [4, 6, 8, 24, 12, 2]
print(largest(x))
    