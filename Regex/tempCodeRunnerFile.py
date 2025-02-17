import re

target_string = "8000 dollar"

#To match all digits
regex_pattern = r'\d'
result = re.findall(regex_pattern,target_string)
print("Matching value", result)

#To match all numbers
regex_pattern = r'\d+'
result = re.findall(regex_pattern,target_string)
print("Matching value", result)

#To match a 4 digit number
#To match all numbers
regex_pattern = r'\d{4}'
result = re.findall(regex_pattern,target_string)
print("Matching value", result)
