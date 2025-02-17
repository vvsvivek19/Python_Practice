import re

# . dot metacharacter
target_string = "Emma loves \n Python"
regex_pattern = r"."
#--dot(.) metacharacter to match any character
result = re.findall(regex_pattern,target_string)
print(result)
result = re.search(regex_pattern,target_string)
print(result.group())
regex_pattern = r".+"
result = re.findall(regex_pattern,target_string)
print(result)
result = re.search(regex_pattern,target_string)
print(result.group())
'''
If you want the DOT to match the newline character as well, use the re.DOTALL or re.S flag as an argument inside the search() method. Let’s try this also.
'''
target_string = "Emma is a Python developer \n She also knows ML and AI"
result = re.search(regex_pattern,target_string,re.S)
print(result.group())

# ^ caret metacharacter
'''
In Python, the caret operator or sign is used to match a pattern only at the beginning of the line.
'''
import re

target_string = "Emma is a Python developer \n Emma also knows ML and AI"
regex_pattern = r"^\w{4}" # caret (^) matches at the beginning of a string
#Matching a 4 letter word at the beginning of the string
result = re.search(regex_pattern,target_string) 
print(result.group())
#Matching a 4 letter word at the beginning of each line
result = re.findall(regex_pattern,target_string,re.M) 
print(result)

# $ dollar metacharacter
'''
The dollar ($) operator or sign matches the regular expression pattern at the end of the string. 
'''
import re
target_string = "Emma is a Python developer \n Emma also knows ML and AI"
regex_pattern = r"\w{2}$"
#Matching a 2 letter word at the end of the string
result = re.search(regex_pattern,target_string) 
print(result.group())
#regex pattern To match a two-letter word at the end of each line 
regex_pattern = r"\b\w{2}\b$"
target_string = """This is an example
Go to my PC
He is at it
I am in"""
result = re.findall(regex_pattern,target_string,re.M) 
print(result)

# * asterisk/star metacharacter