import os
size = os.stat(r'D:\Web Development\Tutorial Practice Codes\Python_Practice\new_file.txt').st_size
if size == 0:
    print("File is empty!!!")
else:
    print("File is not empty")