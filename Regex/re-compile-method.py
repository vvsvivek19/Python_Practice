import re

str1 = "Vivek's lucky numbers are 251 761 231 451"
string_pattern = r"\d{3}"

regex_pattern = re.compile(string_pattern)
print(type(regex_pattern))

res = regex_pattern.findall(str1)
print(res)