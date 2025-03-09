from threading import *
from time import sleep

e = Event()

def light_switch():
    while True:
        print("Light is green 🟢")
        e.set()
        sleep(3)
        print("Light is red 🔴")
        e.clear()
        sleep(3)
        e.set()

def traffic_message():
    e.wait()
    while e.is_set():
        print("You can go")
        sleep(0.5)
        e.wait()
        
t1 = Thread(target= light_switch)
t2= Thread(target=traffic_message)

t1.start()
t2.start()