'''
1
22
333
4444
55555
'''

for i in range(1,6):
    print('')
    for j in range(i):
        print(i,end='')

'''
Print following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
rows = int(input("\n\nEnter how many rows you want? - "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print('')

'''
Print following pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

rows = int(input("\n\nEnter how many rows you want? - "))

for i in range (1,rows+1):
    for j in range(rows + 1 -i,0,-1):
        print(j,end=' ')
    print('')
    