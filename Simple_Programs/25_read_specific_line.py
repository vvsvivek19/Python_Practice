with open(r'D:\Web Development\Tutorial Practice Codes\Python_Practice\test.txt','r') as fp:
    lines = fp.readlines()
count = 0
for line in lines:
    count += 1
    if count == 4:
        print(line)
    else:
        continue