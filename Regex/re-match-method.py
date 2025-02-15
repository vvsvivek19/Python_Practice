"""
There are multiple methods to match pattern in a string:
1. match(pattern, str) - Matches pattern only at the beginning of the string
2. search(pattern, str) - Matches pattern anywhere in the string. Return only first match
3. search(pattern$, str) - Dollar ($) matches pattern at the end of the string.
4. findall(pattern, str) - Returns all matches to the pattern
5. findall(^pattern, str, re.M) - Caret (^) and re.M flag to match the pattern at the beginning of each new line of a string
6. fullmatch(pattern, str) - Returns a match object if and only if the entire target string matches the pattern.
"""

import re

str1 = "Emma is a basketball player who was born on June 17"
regex_pattern = r"\w{4}"
'''
The \w is a regex special sequence that represents any alphanumeric character meaning letters (uppercase or lowercase), digits, and the underscore character.
Then the 4 inside curly braces say that the character has to occur exactly four times in a row (four consecutive characters).
'''
# printing the Match object
res = re.match(regex_pattern,str1)
print("match object:",res)

# Extract match value
print("Match value: ",res.group())

#searching a pattern anywhere in the string - use search or findall method for this
target_string = "Jessa loves Python and pandas"
regex_pattern = r"\w{6}"

#using match
print("With match:")
res = re.match(regex_pattern,target_string)
print(res)

#using search
print("With search")
res = re.search(regex_pattern,target_string)
print(res)
print(res.group())

#using findall
print("With findall")
res = re.findall(regex_pattern,target_string)
print(res)

#match regex at the end of the string - to check if a string ends with a specific word, number or character
import re

target_string = "Emma is a basketball player who was born on June 17, 1993"
regex_pattern = r"\d{4}"

res = re.search(r"\d{4}$",target_string)
print(res)
print("Matching number: ", res.group())
res = re.search(r"player",target_string)
print(res)

#Match regex pattern that starts and ends with the given text
'''
we can create regex pattern for this using meta characters ^ and $. Caret metacharacter to match at the start. Dollar metacharacter to match at the end.
'''
import re
# string starts with letter 'p' ends with letter 's'
def starts_ends_with(str1):
    res = re.match(r"^(P).*(S)$",str1,re.I)
    if res:
        print(res)
        print(res.group())
        print(res.start())
        print(res.end())
        print(res.span())
    else:
        print("None")
starts_ends_with("PYnative is for Python developers")
starts_ends_with("PYnative is for Python")