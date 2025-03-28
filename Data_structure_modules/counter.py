# Write a function that takes a string and returns a dictionary with the frequency of each word. 
# Ignore case and punctuation.

from collections import Counter
import re
text = "Hello world! Hello everyone. This is a test. Hello again."

def frequency(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())  
    sequence = cleaned_text.split()
    obj = Counter(sequence)
    return obj

print(frequency(text))


#Given a list of numbers, find the most frequently occurring number. If multiple numbers have the 
# same highest frequency, return any one of them.
from collections import Counter
nums = [4, 2, 2, 8, 4, 4, 2, 8, 8, 8, 8]

def common(sequence):
    obj = Counter(sequence)
    common_element = obj.most_common(1)[0]
    print(f"Most common element is {common_element[0]} with {common_element[1]} occurences")

common(nums)

#Given two strings, one original and one modified with some letters removed, find out which letters 
#are missing using Counter.
from collections import Counter

original = "mississippi"
modified = "msssppi"

original_obj = Counter(original)
modified_obj = Counter(modified)
print(original_obj)
print(modified_obj)

missing_letters = original_obj - modified_obj

print(dict(missing_letters))

#Write a function that checks if two strings are anagrams of each other (i.e., they contain the 
# same characters with the same frequency).

from collections import Counter

def is_anagram(str1, str2):
    obj1 = Counter(str1)
    obj2 = Counter(str2)
    return obj1 == obj2

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))    

