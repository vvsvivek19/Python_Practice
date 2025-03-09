#import Thread class
from threading import Thread,current_thread

#Create a function containing code to be executed parallely
def display(n,mgs):
    print("t1 thread details:",current_thread())
    for i in range(n):
        print(mgs)
#Create a new thread here
t1 = Thread(target=display,args=(5,"hello"))
#start the new thread
t1.start()

for i in range(4):
    print("world")