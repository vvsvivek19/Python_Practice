import re

target_string = "Emma is a basketball player who was born on June 17."
res = re.search(r"(\w{10}).+(\d{2})",target_string)
print(res.group(1))
print(res.group(2))