import re
target_str = "My roll number is 25 and my date of birth is 19 Feb"
# extract mathing value
res = re.findall(r"\d",target_str)
print(res)

'''
To avoid issues, always write a regex pattern using a raw string. 
'''
target_str = r"D:\Web Dev\Tutorial Practice Codes\Python_Practice\Regex"
#pattern = r"^D:\\Web Dev\\Tutorial Practice Codes"
pattern = re.escape("D:\Web Dev\Tutorial Practice Codes")
res = re.search(pattern,target_str)
print(res.group())

'''
Some more regex methods examples
'''
# import the RE module
import re

target_string = "Jessa salary is 8000$"

# compile regex pattern
# pattern to match any character
str_pattern = r"\w"
pattern = re.compile(str_pattern)

# match regex pattern at start of the string
res = pattern.match(target_string)
# match character
print(res.group())  
# Output 'J'

# search regex pattern anywhere inside string
# pattern to search any digit
res = re.search(r"\d", target_string)
print(res.group())
# Output 8

# pattern to find all digits
res = re.findall(r"\d", target_string)
print(res)  
# Output ['8', '0', '0', '0']

# regex to split string on whitespaces
res = re.split(r"\s", target_string)
print("All tokens:", res)
# Output ['Jessa', 'salary', 'is', '8000$']

# regex for replacement
# replace space with hyphen
res = re.sub(r"\s", "-", target_string)
# string after replacement:
print(res)
# Output Jessa-salary-is-8000$
# replace space with hyphen
res = re.subn(r"\s", "-", target_string)
# string after replacement:
print(res)
