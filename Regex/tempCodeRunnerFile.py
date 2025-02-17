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