import re
target_str = "My roll number is 25 and my date of birth is 19 Feb"
# extract mathing value
res = re.findall(r"\d",target_str)
print(res)