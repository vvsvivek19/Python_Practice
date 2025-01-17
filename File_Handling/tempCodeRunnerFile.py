import time
from datetime import datetime

log_file = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\log.txt"
messages = ["INFO: Task completed", "ERROR: Something went wrong", "DEBUG: Value updated"]

with open(log_file,'w') as file:
    for index in range(10):
        log_message = f"{datetime.now()}:{messages[index % len(messages)]}\n"
        print(log_message,end='')
        file.write(log_message)
        time.sleep(1)
print("Log file generated with timestamps and messages.")
