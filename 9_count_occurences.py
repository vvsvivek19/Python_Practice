str_x = "Emma is good developer. Emma is a writer"

#method 1 using count:
def count_chars(user_string,word):
    occurence = user_string.count(word)
    return occurence

word = input('Enter a word to be counted: ')
print(f"The word '{word}' occurs {count_chars(str_x,word)} times")


#method 2 using regex module:
import re

matches = re.findall(word,str_x)
l = len(matches)
print(f"The word '{word}' occurs {l} times")

#method 3 without using string module or regex
count = 0
print("Given statement is:",str_x)
for i in range(len(str_x)-1):
    if str_x[i:i+4] == word:
        count += 1

print(f"The word '{word}' occurs {count} times")
    

