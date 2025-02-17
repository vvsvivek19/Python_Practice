import re

#By capturing groups we can match several distinct patterns inside the same target string.

target_string = "The price of PINEAPPLE ice cream is 20"

# two groups enclosed in separate ( and ) bracket
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

# Extract matching values of all groups
print(result.groups())
# Output ('PINEAPPLE', '20')

# Extract match value of group 1
print(result.group(1))
# Output 'PINEAPPLE'

# Extract match value of group 2
print(result.group(2))

#Regex Capture Group Multiple Times
'''
Note: Don’t use the findall() method because it returns a list, the group() method cannot be applied. If you try to apply it to the findall method, you will get AttributeError: ‘list’ object has no attribute ‘groups.’
'''
target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"
# two groups enclosed in separate ( and ) bracket
# group 1: find all uppercase letter
# group 2: find all numbers
# you can compile a pattern or directly pass to the finditer() method
pattern = re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")
# find all matches to groups
for match in pattern.finditer(target_string):
    # extract words
    print(match.group(1))
    # extract numbers
    print(match.group(2))