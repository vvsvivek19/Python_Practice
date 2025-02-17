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
import re
# -- to match all the numbers from a string string using an asterisk (*) metacharacter. 
regex_pattern = r"\d\d*"
'''
Pattern Explaination:
pattern is made of two consecutive \d. The \d special sequences represent any digit.

The most important thing to keep in mind here is that the asterisk (*) at the end of the pattern means zero or more repetitions of the preceding expression. And in this case, the preceding expression is the last \d, not all two of them.

This means that we are basically searching for numbers with a minimum of 1 digit and possibly any integer.
'''
target_string = "Numbers are 8,23, 886, 4567, 78453"
result = re.findall(regex_pattern,target_string)
print(result)

# + plus metacharacter
'''
The plus operator (+) inside a pattern means that the preceding expression or character should repeat one or more times with as many repetitions as possible, meaning it is a greedy repetition.
'''
import re
# regex pattern to match 2 or more digits numbers in a target string
regex_pattern = r"\d\d+" 
target_string = "Numbers are 8,23, 886, 4567, 78453"
result = re.findall(regex_pattern,target_string)
print(result)

# ? Question mark metacharacter
'''
question mark operator or sign (?) inside a regex pattern means the preceding character or expression to repeat either zero or one time only. This means that the number of possible repetitions is strictly limited on both ends.
'''
import re
# regex pattern to match 4 or 5 digits numbers in a target string
regex_pattern = r"\d\d\d\d\d?" 
target_string = "Numbers are 8,23, 886, 4567, 78453"
result = re.findall(regex_pattern,target_string)
print(result)

# \ backslash metacharacter
'''
Backslash metacharacter has two primary purposes inside regex patterns:
- It can signal a special sequence being used, for example, \d for matching any digits from 0 to 9.
- If your expression needs to search for one of the special characters, you can use a backslash ( \ ) to escape them. For example, you want to search for the question mark (?) inside the string. You can use a backslash to escaping such special characters because the question mark has a special meaning inside a regular expression pattern.
'''
import re
target_string =  "Emma is a Python developer. Emma salary is 5000$. Emma also knows ML and AI."
# escape dot
regex_pattern = r"\."
result = re.split(regex_pattern,target_string)
print(result)

# [] square brackets
'''
The square brackets are beneficial when used in the regex pattern because they represent sets of characters and character classes.
'''
import re
target_string = "The square brackets are beneficial when used in the regex pattern because they represent sets of characters and character classes."
regex_pattern = r"[T c]"
result = re.findall(regex_pattern,target_string)
print(result)