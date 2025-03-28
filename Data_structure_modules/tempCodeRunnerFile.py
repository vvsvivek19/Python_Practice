from collections import Counter

def is_anagram(str1, str2):
    obj1 = Counter(str1)
    obj2 = Counter(str2)
    return obj1 == obj2

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False