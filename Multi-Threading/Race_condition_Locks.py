from threading import *
lock = Lock()
class Bus:
    def __init__(self,name,available_seats,l):
        self.name = name
        self.available_seats = available_seats
        self.l = l
    def reserve(self,need_seats):
        self.l.acquire()
        nm = current_thread().name
        print("Available seats are:",self.available_seats)
        if self.available_seats >= need_seats:
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry!! Seats are not available.")
        self.l.release()
b1 = Bus("Maha Lakshmi Travels",4,lock)
t1 = Thread(target=b1.reserve,args=(2,),name="Jay")
t2 = Thread(target=b1.reserve,args=(2,),name="Raj")

t1.start()
t2.start()