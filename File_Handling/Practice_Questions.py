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
    file.writelines(lines)
    file.seek(0)
    content = file.read()
    print("Content after:")
    print(content)
#efficient code
# with open(file_path, "r+") as file:
#     lines = [line for line in file if line.strip()]
#     file.seek(0)
#     file.writelines(lines)
#     file.truncate()
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

#SOLUTION 9: Merge two files

file_path_1 = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
file_path_2 = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\MyData.txt"
merged_file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\Merged_file.txt"

with open(file_path_1,"r") as file:
    content_1 = file.readlines()
with open(file_path_2,"r") as file:
    content_2 = file.readlines()
with open(merged_file_path,"w+") as file:
    file.writelines(content_1)
    file.writelines(content_2)
    file.seek(0,0)
    content = file.read()
    print(content)

#SOLUTION 10: Find and Replace
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\CatPoem.txt"
with open(file_path,"r+") as file:
    lines = file.readlines()
    # print(lines)
    updated_lines = [item.lower().replace("cat","bat") for item in lines]
    file.seek(0,0)
    file.writelines(updated_lines)
    file.truncate()
with open(file_path,"r") as file:
    lines = file.read()
    print(lines)
    
#SOLUTION 11

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\logFile.txt"
# error_lines = []
with open(file_path,"r") as file:
    lines = file.readlines()
    error_lines = [item.strip("\n") for item in lines if "ERROR" in item]
    # for item in lines:
    #     if "ERROR" in item:
    #         error_lines.append(item)
print("Error lines are:")
for item in error_lines:
    print(item)

#SOLUTION 12: JSON File handling

import json
try:
    filePath = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\sample.json"

    data = [{"Name": "Alice", "Age": 25, "City": "New York", "Country": "USA", "Profession": "Software Engineer"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles", "Country": "USA", "Profession": "Data Scientist"}]

    #Reading the existing data of json file
    try:
        with open(filePath,"r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    for item in data:
        existing_data.append(item)
    #updating the json file with new data
    with open(filePath, "w") as file:
        json.dump(existing_data,file,indent=4)
    
    # Read and modify JSON data
    with open(filePath,"r") as file:
        new_data = json.load(file)
    #Updating Bob's Age
    for record in new_data:
        if record["Name"] == "Bob":
            record["Age"] = 31
    #Saving updated data
    with open(filePath, "w") as file:
        json.dump(new_data,file,indent=4)
except Exception as msg:
    print(msg)

#SOLUTION 13 - CSV File manipulation

import csv

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\data.csv"

#opening the existing CSV file
with open(file_path, "w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","city"])
    writer.writerow(["Vivek",25,"Kanpur"])
    writer.writerow(["Alice",25,"New York"])

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\data.csv"
import csv
#Add a new row
with open(file_path,"a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 28, "Chicago"])

#Read and print content
with open(file_path,"r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Updating existing data in the file
rows = []
with open(file_path,"r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "Vivek":
            row[1] = 26
        rows.append(row)

with open(file_path,"w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

#SOLUTION 15 - Binary file handling
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\binary_file.bin"
#binary data
data = b"Hello,how are you? This is biinary data"
with open(file_path,"wb") as file:
    file.write(data)

#reading data from binary file
with open(file_path,"rb") as file:
    file_data = file.read()

print("Binary data->",file_data)
    
#SOLUTION 16 - File compression
import gzip
import shutil

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\text.txt"
compressed_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\compressed_text.txt.gz"
decompressed_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\decompressed_text.txt"

data = b"""In a world of swirling galaxies and dancing stars, a lone adventurer, armed with nothing but wit and a rusty compass, embarked on a journey across uncharted lands. He faced perils untold  treacherous rivers, treacherous mountains, and creatures of myth and legend. Yet, with each step, his resolve grew stronger, fueled by an insatiable thirst for knowledge and a yearning for the unknown. He sought not fortune or fame, but the thrill of discovery, the joy of pushing the boundaries of the known."""

#writing data in binary file
with open(file_path, "wb") as file:
    file.write(data)

#compressing the file
with open(file_path,"rb") as file_in:
    with gzip.open(compressed_path,"wb") as file_out:
        shutil.copyfileobj(file_in,file_out)

print("Compression done successfully")

#decompressing the file
with open(compressed_path,"rb") as file_in:
    with gzip.open(decompressed_path,"wb") as file_out:
        shutil.copyfileobj(file_in,file_out)
print("Decompression done successfully")

#SOLUTION 17 - Encryption and Decryption
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\text.txt"
encrypted_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\encrypted_text.txt"
decrypted_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\decrypted_text.txt"

#reading data from file and encrypt it
with open(file_path,'rb') as file:
    data = file.read()

encrypted_data = cipher.encrypt(data)

#writing encrypted data in a encrypted file
with open(encrypted_path,'wb') as file:
    file.write(encrypted_data)

#decrypting data
with open(encrypted_path,'rb') as file:
    encrypted_data = file.read()

decrypted_data = cipher.decrypt(encrypted_data)

#writing decrypted data into an another file
with open(decrypted_path,'wb') as file:
    file.write(decrypted_data)

#reading data from decrypted file
with open(decrypted_path,"rb") as file:
    decrypted_data = file.read()

print("File encryption and decryption successful")
print("Printing drcypted data")
print(decrypted_data)

#SOLUTION 18 - Directory Operations
import os
dir_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling"
output_file = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\file_list.txt"

files = os.listdir(dir_path)

with open(output_file,"w") as file:
    for name in files:
        file.write(name + "\n")

print("All the files name from give directory path are written to file_list.txt")

#SOLUTION 19 - Removing duplicate text
file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\duplicate_text.txt"
output_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\unique_text.txt"
with open(file_path, 'r') as file:
    all_lines = file.readlines()
unique_lines = list(set(all_lines))
with open(output_path,'w') as file:
    file.writelines(unique_lines)
print("Duplicate lines removed and saved to a new file.")

#SOLUTION 20 - Custom Log Generator
import time
from datetime import datetime

log_file = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\log.txt"
messages = ["INFO: Task completed", "ERROR: Something went wrong", "DEBUG: Value updated"]

with open(log_file,'w') as file:
    for index in range(10):
        log_message = f"{datetime.now()}:{messages[index % len(messages)]}\n"
        print(log_message,end='')
        file.write(log_message)
        time.sleep(1)
print("Log file generated with timestamps and messages.")
