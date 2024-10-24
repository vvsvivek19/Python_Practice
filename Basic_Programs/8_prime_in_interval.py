from math import sqrt
def check_prime(num):
    """
    Check whether a given number is prime.

    A prime number is a number greater than 1 that has no divisors other than 1 and itself. 
    To determine whether a number n is prime, we need to check if it has any divisors other 
    than 1 and n.

    Key Concept:
    If a number n can be factored into two factors a and b such that:
        n = a × b
    Then, at least one of those factors must be less than or equal to sqrt(n). 
    This is because if both factors were greater than sqrt(n), their product would exceed n.

    Example:
    - 36 = 6 × 6, so both factors are exactly sqrt(36) = 6.
    - 28 = 4 × 7. Here, one factor (4) is less than sqrt(28) ≈ 5.29.

    Thus, if no factors exist below sqrt(n), the number is prime. Any factor pair greater 
    than the square root would have already been found as a reverse pair (like 4 and 7 for 28).

    Why is this efficient?
    Instead of checking all numbers from 2 to n-1, you only need to check up to sqrt(n).
    This drastically reduces the number of checks, especially for large numbers. 
    For example, for n = 997, instead of checking 995 numbers, you only need to check 
    up to sqrt(997) ≈ 31.6 (i.e., numbers from 2 to 31).

    :param num: int - The number to check for primality.
    :return: int - Returns 1 if the number is prime, otherwise 0.
    """
    if num < 2:
        return 0
    flag = 0
    i = 2
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1
start = int(input("Enter starting range: "))
end = int(input("Enter the end range: "))
for i in range(start, end):
    if(check_prime(i)):
        print(i,end=" ")
    