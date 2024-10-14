def palindrome(num):
    reverse = 0
    temp = num

    while temp > 0:
        rem = temp % 10
        reverse = (reverse * 10) + rem
        temp = temp // 10

    if num == reverse:
        print('Number is Palindrome')
    else:
        print('Number is not a Palindrome')

num = int(input("Enter a Number: "))
palindrome(num)