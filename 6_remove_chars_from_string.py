print('Program to remove n characters from the starting of a string')
user_string = input('Enter any character string: ')
num_of_characters = int(input('Enter number of characters from string: '))

def remove_chars(user_string,num_of_characters):
    print('String after character removal:',user_string[num_of_characters::])

remove_chars(user_string,num_of_characters)