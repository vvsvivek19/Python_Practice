def div_five(user_list):
    print('Numbers divisible by 5 in the list are:')
    for i in user_list:
        if i % 5 == 0:
            print(i)

div_five([10, 20, 33, 46, 55])