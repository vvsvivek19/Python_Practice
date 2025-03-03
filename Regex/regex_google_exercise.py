import re
file = open(r"D:\Web Dev\Tutorial Practice Codes\Python_Practice\Regex\Popular Baby Names.html","r")
content = file.read()
all_names = re.findall(r'<td>(\d+)</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',content)
print(all_names)
male_names = {}
for name in all_names:
    male_names[name[0]] = name[1]
for item in male_names.items():
    print(f"{item[0]}-{item[1]}")
print("=================================================================")
female_names = {}
for name in all_names:
    female_names[name[0]] = name[2]
for item in female_names.items():
    print(f"{item[0]}-{item[1]}")