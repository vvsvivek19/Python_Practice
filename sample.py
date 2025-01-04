mylist = ['John', 15, 16.6, True, 'Vivek', 5+7j, 'Eric']
print(mylist[-2])
mylist[-3] = 'Singh'
print(mylist[-3])
mylist[-3] = 'Vivek'
print(mylist[-3])
list1 = list((1,2,3,4,5))
print(list1)
print(mylist) 
list3 = mylist + ['Singh']
print(list3)

mylist = ['John', 15, 16.6, True, 'Vivek', 5+7j, 'Eric']
for x in mylist:
    print(x,end=' ')
print('')
for i in range(-1,-len(mylist),-1):
    print(mylist[i],end=' ')

L1 = [1,2,3,4,5]
print(L1)
L1[len(L1):] = [6]
print(L1)
L1[0:2].clear()
print(L1)

text = """Beautiful is better than ugly 
Explicit is better than implicit Simple is 
better than complex Complex is better than complicated """.lower()
unique_words = set()
for words in text.split():
    unique_words.add(words)
print(unique_words)