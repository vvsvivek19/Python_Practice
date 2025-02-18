import re
target_string = """ For instance, considering the same target string, we can search for the word “ssa” using a \b special sequence like this "\bssa\b". But we will not get a match because non-alphanumeric characters do not border it on both sides"""
regex_pattern = r"\b\w{6}\b"
result = re.findall(regex_pattern,target_string)
print(result)

# \B
result = re.findall(r"\Bthon", target_string)
print(result)