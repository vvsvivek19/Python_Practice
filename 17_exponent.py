def exponent(base,exp):
    return base ** exp
base = int(input("Enter Base: "))
exp = int(input("Enter exponent: "))
print(f"{base} raises to the power of {exp}: {exponent(base,exp)} i.e.",end=' ')
for x in range(exp):
    if x == exp - 1:
        print(f'{base} = {exponent(base,exp)}',end='')
    else:
        print(f'{base} * ',end='')