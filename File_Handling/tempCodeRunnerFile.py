file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\TestData.txt"
lines = []
with open(file_path,"r") as file:
    all_lines = file.readlines()
    for item in all_lines:
        if item != '\n':
            lines.append(item)
with open(file_path,"w+") as file:
    all_lines = file.readlines()
    print("Content before:")
    for item in all_lines:
        print(item)
    file.writelines(lines)
    file.seek(0)
    content = file.read()
    print("Content after:")
    print(content)