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