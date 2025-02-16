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
'''
we used [] meta character to indicate a list of delimiter characters. The [] matches any single character in brackets. For example, [-;,.\s] will match either hyphen, comma, semicolon, dot, and a space character.
'''
result = re.split(delimiter,target_string)
print(result)

#Regex to split String into words with multiple word boundary delimiters
target_string = "PYnative! dot.com; is for, Python-developer?"
delimiter = r"[\b\W\b]+"
'''
The \W is a regex special sequence that matches any Non-alphanumeric character. Non-alphanumeric means no letter, digit, and underscore. [\b\W\b]+ regex pattern to caters to any Non-alphanumeric delimiters. 
'''
result = re.split(delimiter,target_string)
print(result)

#Split strings by delimiters and specific word
target_string = "12, and45,78and85-17and89-97"
# --- split by word 'and' space, and comma
delimiter = r"and|[\s,-]+"
result = re.split(delimiter,target_string)
print(result)

#Regex split a string and keep the separators
'''
In simple terms, be careful while using the re.split() method when the regular expression pattern is enclosed in parentheses to capture groups. If capture groups are used, then the matched text is also included in the resulted list.
It is helpful when you want to keep the separators/delimiter in the resulted list.
'''
#-- including the pattern without parentheses
target_string = "12-45-78."
delimiter = r"\D+"
result = re.split(delimiter,target_string)
print("When pattern is not in parenthesis:",result)
#-- including the pattern with parentheses
target_string = "12-45-78."
delimiter = r"(\D+)"
result = re.split(delimiter,target_string)
print("When pattern is in parenthesis:",result)

#Regex split string by ignoring case
# Without ignoring case
print("Without ignoring case:",re.split('[a-z]+', "7J8e7Ss3a"))
# output ['7J8', '7S', '3', '']

# With ignoring case
print("With ignoring case:",re.split('[a-z]+', "7J8e7Ss3a", flags=re.IGNORECASE))
# output ['7', '8', '7', '3', '']