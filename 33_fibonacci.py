total_terms = int(input("Enter total numbers in fibonacci you want: "))
first_term = 0
second_term = 1
print(f'{first_term} {second_term}',end=' ')
for i in range(2,total_terms):
    term_sum = first_term + second_term
    print(term_sum, end=' ')
    first_term = second_term
    second_term = term_sum