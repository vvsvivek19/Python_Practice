
#nested function
def outer_func(a_outer,b_outer):
    def inner_func(a_inner,b_inner):
        total_sum = a_inner + b_inner
        return total_sum
    res = inner_func(a_outer,b_outer)
    return res + 5
result = outer_func(10,20)
print("Sum:",result)

#recursion
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
print(recursive_sum(10))

#assigning function new name:
def display_student(name, age):
    print(name, age)
display_student('Vivek',25)
show_student = display_student
show_student('Singh',24)
