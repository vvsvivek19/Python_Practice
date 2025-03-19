from threading import *
from time import sleep

def write_data():
    con.acquire()    
    with open("weekly_temperature.txt","w") as file:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for day in days:
            temp = input(f"Please enter the temperature for {day}: ")
            file.write(temp + "\n")     
    con.notify_all()
    con.release()

def max_temp():
    con.acquire() 
    con.wait(timeout=0)  
    with open("weekly_temperature.txt","r") as file:
        temp_data = file.readlines()
        modified_data = []
        for data in temp_data:
            modified_data.append(int(data.strip("\n")))
        maximum_temp = max(modified_data)
    print("Maximum temperature: ",maximum_temp)
    con.release()

def avg_temp():
    con.acquire()    
    con.wait(timeout=0) 
    with open("weekly_temperature.txt","r") as file:
        temp_data = file.readlines()
        modified_data = []
        for data in temp_data:
            modified_data.append(int(data.strip("\n")))
        avg = sum(modified_data)/len(modified_data)
    print("Maximum temperature: ",avg)  
    con.release()

con = Condition()
t1 = Thread(target=write_data)
t2 = Thread(target=max_temp)
t3 = Thread(target=avg_temp)

t1.run()
t2.run()
t3.run()