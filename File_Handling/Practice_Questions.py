# SOLUTION 1: Creating a new file and adding content to that file
try:
    with open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt", "w+") as file:
        content = "Hello, World!\nWelcome to Python file handling\n"
        file.write(content)
        file.seek(0)
        read_content = file.read()
        print(read_content)
except Exception as msg:
    print("Error Occured ->", msg)

# SOLUTION 2: Appending lines to a file
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"

with open(file_path,"a+") as file:
    content = ["This is an appended line.\n","File handling is easy in Python.\n"]
    file.writelines(content)
    file.seek(0)
    read_content = file.read()
    print(read_content)

#SOLUTION 3: Read content of the file line by line
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
try:
    with open(file_path,"r") as file:
        content = file.readlines()
        print("CONTENT IS:")
        for item in content:
            print(item.strip("\n"))
except Exception as msg:
    print("Error Occured ->", msg)

#SOLUTION 4: Count lines, words and characters
'''
Content of the file is
----------------------
Hello, World!
Welcome to Python file handling
This is an appended line.
File handling is easy in Python.
'''
import re
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestDataCopy.txt"
total_lines = 0
total_words = 0
total_characters = 0
try:
    with open(file_path,"r") as file:
        content = file.readlines()
        total_lines = len(content)
        for item in content:
            line_list = item.strip("\n").split()
            line_characters = re.sub(r'[^\w]', '', item)
            total_words = total_words + len(line_list)
            total_characters = total_characters + len(line_characters)
    print("Total Lines ->",total_lines)
    print("Total words ->",total_words)
    print("Total characters ->",total_characters)
            
except Exception as msg:
    print("Error Occured ->", msg)
    
#SOLUTION 5: Copying content of one file to another
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
with open(file_path, "r") as file:
    content = file.read()
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestDataCopy.txt"
with open(file_path,"w+") as file:
    file.write(content)
    file.seek(0)
    copied_content = file.read()
    print(copied_content)

#SOLUTION 6: Search for a word in a file

'''
content of the file is:
-----------------------
Hello, World!
Welcome to Python file handling
This is an appended line.
File handling is easy in Python.
This is the first line of the text file.
This is the second line of the text file. 
This is the third line of the text file.
This is the fourth line of the text file.
This is the fifth line of the text file.
This is the sixth line of the text file.
This is the seventh line of the text file.
This is the eighth line of the text file.
This is the ninth line of the text file.
This is the tenth line of the text file.
This is the eleventh line of the text file.
This is the twelfth line of the text file.
This is the thirteenth line of the text file.
This is the fourteenth line of the text file.
This is the fifteenth line of the text file.
This is the sixteenth line of the text file.
This is the seventeenth line of the text file.
This is the eighteenth line of the text file.
This is the nineteenth line of the text file.
This is the twentieth line of the text file.
'''
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
with open(file_path,"r") as file:
    lines = file.readlines()
    word = "This"
    found_at = []
    for index,item in enumerate(lines):
        if word.lower() in item.lower():
            found_at.append(index)
    print(f"Word {word} was found at line numbers: ",end='')
    for index in found_at:
        print(index, end = ",")

#SOLUTION 7: Read a FILE in reverse order
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
with open(file_path,"r") as file:
    content = file.read()
    print(content[::-1])
#efficient solution for large files
# with open(file_path, "r") as file:
#     for line in reversed(file.readlines()):
#         print(line.strip())

#SOLUTION 8: Remove blank lines
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
lines = []
with open(file_path,"r") as file:
    all_lines = file.readlines()
    for item in all_lines:
        if item.strip():
            lines.append(item)
with open(file_path,"w+") as file:
    content = file.read()
    print("Content before:")
    print(content)
    file.writelines(lines)
    file.seek(0)
    content = file.read()
    print("Content after:")
    print(content)
'''
How It Works:
item.strip():
    The strip() method removes any leading and trailing whitespace characters (including spaces, tabs, 
    and newline characters \n) from the string item.
    If item contains only whitespace (e.g., " " or "\n"), item.strip() will return an empty string ("").
Condition if item.strip()::
    In Python, an empty string ("") is considered False in a boolean context.
    Non-empty strings (e.g., "Hello" or "This is a line") are considered True.
    Thus, if item.strip(): checks if the line has non-whitespace content.
lines.append(item):
    If the condition if item.strip(): is True (meaning the line contains meaningful text), the item 
    (line) is added to the lines list using the append() method.
'''
    
    