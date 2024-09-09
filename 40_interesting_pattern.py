'''
Print following pattern
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
rows = int(input("Enter how many rows you want?: "))
mid = 0
if rows % 2 == 0:
    mid = rows // 2
else:
    mid = (rows // 2) + 1

for i in range(rows):
    print('')
    if i+1 >= mid:
        for k in range(rows - i):
            print('*',end='')
    else:
        for j in range(i+1):
            print("*",end='')