list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for i in list1:
    if i % 2 != 0:
        list3.append(i)
for j in list2:
    if j % 2 == 0:
        list3.append(j)
print('List 1 is:',list1)
print('List 2 is:',list2)
print('New list is:',list3)