# Prompt the user to enter a string and store it in 'user_string'
user_string = input('Enter any character string: ')

# Method 1: Using enumerate() to print characters at even indices
print("Printing only even index chars with method 1")

# Loop through each character in the string with its index using enumerate
for idx, item in enumerate(user_string):
    # Check if the index is even
    if idx % 2 == 0:
        # Print the character at the even index
        print(item)

# Method 2: Using a range-based loop to print characters at even indices
print("Printing only even index chars with method 2")

# Get the length of the string
l = len(user_string)

# Loop through the string with a step of 2, starting from index 0 to the second-to-last index
for i in range(0, l-1, 2):
    # Print the character at the even index
    print(user_string[i])

# Method 3: Using slicing to print characters at even indices
print("Printing only even index chars with method 3")

# Slice the string to get every second character, starting from index 0
for i in user_string[::2]:
    # Print each character obtained from the slice
    print(i)
