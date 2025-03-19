from threading import Thread
from time import sleep

def upload():
    print("Upload starts....")
    sleep(3)
    print("Video Uploaded!")

def notification():
    print("\nSending notification to suscriber!!!\n")

t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()

for i in range(4):
    print("Main thread is running")