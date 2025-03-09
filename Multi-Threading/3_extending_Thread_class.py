from threading import Thread
from time import sleep
videos = ['OOP Syllabus','constructor','destructor','File handling']

class MyClass(Thread):
    def __init__(self,val):
        print("constructor called")
        self.kid = val
        Thread.__init__(self)
    
    def compression(self):
        print("Video compression code working")
    
    def run(self):
        self.compression()
        if self.kid == True:
            print("Suitable for kids")
        for video in videos:
            print(f"{video} started uploading....")
            sleep(2)
            print(f"{video} uploaded")

t1 = MyClass(True)
t1.start()

for i in range(4):
    sleep(0.5)
    print("Checking copyright...")