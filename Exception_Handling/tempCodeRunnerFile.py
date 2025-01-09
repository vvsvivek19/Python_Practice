
try:
    file = open(r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\sample.txt",'a+')
    str1 = '\nPython is easy\nIt is simple\nEverything is an object\n'
    file.write(str1)
    #There is file named sample.txt in the above mentioned path with content
    #This is sample text to test exception handling of opening a file
except FileNotFoundError as msg:
    print(f"{msg}: File not found or it is inaccessible")
else:
    content = file.readlines()
    print(content)
    # for item in content:
    #     print(item, end='')
finally:
    file.close()