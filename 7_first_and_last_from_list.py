numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check_first_last(user_list):
    print("Given List:",user_list)
    if user_list[0] == user_list[-1]:
        print("First and Last numbers of list are same")
    else:
        print("First and Last numbers of list are not same")

check_first_last(numbers_x)
check_first_last(numbers_y)
