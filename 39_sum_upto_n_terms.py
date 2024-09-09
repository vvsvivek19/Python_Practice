num = int(input("Enter total number of terms: "))
total_sum = 0
current_term = 0
for i in range(num):
    current_term = current_term * 10 + 2
    total_sum = total_sum + current_term
print('Sum of series 2 + 22 + 222 + 2222....upto n terms is: ', total_sum)