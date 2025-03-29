from datetime import *

#datetime module has five main classes - date, time, datetime, timedelta and tzinfo

now = datetime.now() #here datetime is a class inside the datetime module
print(now)
print(type(now))

#creating object of date class
date1 = date(2025,4,29)
print(date1) 

#printing current date
current_date = date.today()
print("Date:",current_date)
print("Day:",current_date.day)
print("Month:",current_date.month)
print("Year:",current_date.year)

#working with time
#--using the object of datetime object
now = datetime.now() #now is a class method of the datetime class
print("Current time is:", now.time())
#--creating object of time class
#---time class has following optional arguments: hour, minute, second, microsecond, tzinfo, *, fold
t = time()
print("Time:",t)
#--creating object of time class, but also passing keyword arguments
t = time(hour=14,minute=56,second=43)
print("Time:",t)

#Extract Hours, Minutes, Second from datetime.now() method
#--if have a datetime class object, then from that you can derive just the time
t = datetime.now().time()
print("Current Time is:",t)
print('Hours', t.hour)
print('Minutes', t.minute)
print('Seconds', t.second)
print('Microseconds', t.microsecond)

#Creating object of datetime class
#--we use now classmethod to get current date and time, but to have our date and time we create 
# datetime object
# ---Get current date and time
now = datetime.now()
print('Current datetime:', now)
# ---create datetime object
dt = datetime(year=2021, month=2, day=17, hour=13, minute=47, second=34)
print("Datetime is:", dt)

#Extracting date, time and time stamp from date time
# create datetime object
dt = datetime.now()
print("Datetime is:", dt)
# Get date, time, and timestamp
print('Date:', dt.date())
print('Time:', dt.time())
print('Timestamp:', dt.timestamp())
# Get Attributes
print('Year:', dt.year)
print('Month:', dt.month)
print('Day:', dt.day)
print('Hours:', dt.hour)
print('Minutes:', dt.minute)
print('Seconds:', dt.second)
print('Microseconds:', dt.microsecond)

#create a datetime object from timestamp
ts = 1743252541.717566
dt = datetime.fromtimestamp(ts)
print("The date and time is:", dt)

#Python DateTime Formatting
# --datetime to string
from datetime import datetime
dt = datetime.now()
datetime_str = dt.strftime("%d/%m/%Y %H:%M:%S")
print('DateTime String:', datetime_str)



