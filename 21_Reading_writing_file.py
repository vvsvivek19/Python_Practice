with open(r'D:\Web Development\Tutorial Practice Codes\Python_Practice\test.txt','r') as fp1:
    lines = fp1.readlines()

with open('new_file.txt','w') as fp2:
    count = 0
    for line in lines:
        count += 1
        if count == 4:
            continue
        else:
            fp2.write(line)
