import re

target_string = "My name is maximums and my luck numbers are 12 45 78"
delimiter = r"\s+"
result = re.split(delimiter,target_string)
print(result)

#using the maxsplit parameter to limit the number of splits
target_string = "12-45-78"
delimiter = r"\D" #\D special sequence that matches any non-digit character.
result = re.split(delimiter,target_string,maxsplit=2)
print(result)

#Regex to Split string with multiple delimiters - example - spliting either by hyphen or comma
target_string = "12,45,78,85-17-89"
delimiter = r",|-"
result = re.split(delimiter,target_string) 
print(result)

#Regex to split string on five delimiters 
target_string = "PYnative   dot.com; is for, Python-developer"
delimiter = r"[-;,.\s]\s*"
result = re.split(delimiter,target_string)
print(result)