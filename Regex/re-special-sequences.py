#Special Sequence \A and \Z
import re

target_string = "Jessa is a Python developer, and her salary is 8000"
regex_pattern = r"\A([A-Z].*?)\s"
# \A to match at the start of a string
# match word starts with capital letter
result = re.findall(regex_pattern, target_string)
print("Matching value", result)

regex_pattern = r"\d.*?\Z"
# \Z to match at the end of a string
# match number at the end of the string
result = re.findall(regex_pattern, target_string)
print("Matching value", result)

#Special sequence \d and \D
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
regex_pattern = r'\d{4}'
result = re.findall(regex_pattern,target_string)
print("Matching value", result)

#To match all non-digits
regex_pattern = r'\D'
result = re.findall(regex_pattern,target_string)
print("Matching value", result)

