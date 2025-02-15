import re

# Target String
target_string = "Emma is a baseball player who was born on June 17, 1993."

# find substring 'ball', this doesn't search for a exact match
result = re.search(r"ball", target_string)

# Print matching substring
print(result.group())
# output 'ball'

# find exact word/substring surrounded by word boundary
result = re.search(r"\bball\b", target_string)
if result:
    print(result)
# output None

# find word 'player'
result = re.search(r"\bplayer\b", target_string)
print(result.group())

#searching for multiple patterns together
import re

target_string = "Emma is a basketball player who was born on June 17."
res = re.search(r"(\w{10}).+(\d{2})",target_string)
print(res.group(1))
print(res.group(2))
