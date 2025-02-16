import re

#Replace all the whitespace with a hyphen in a string

target_string = "Jessa knows testing and machine learning"
pattern_to_replace = r"\s"
replacement = "_"
result_str = re.sub(pattern_to_replace,replacement,target_string)
print(result_str)

#Regex to remove whitespaces from a string - includes four cases

#--Remove all spaces, including single or multiple spaces ( pattern to remove \s+ )
target_string = "   Jessa Knows Testing And Machine Learning \t  ."
pattern_to_replace = r"\s+" # \s+ to remove all spaces # + indicate 1 or more occurrence of a space
replacement = ""
result_str = re.sub(pattern_to_replace,replacement,target_string)
print(result_str)

#--Remove leading spaces ( pattern to remove ^\s+ )
target_string = "   Jessa Knows Testing And Machine Learning \t  ."
pattern_to_replace = r"^\s+" # ^\s+ remove only leading spaces # caret (^) matches only at the start of the string
replacement = ""
result_str = re.sub(pattern_to_replace,replacement,target_string)
print(result_str)


#--Remove trailing spaces ( pattern to remove \s+$ )
target_string = "   Jessa Knows Testing And Machine Learning.   \t\n"
pattern_to_replace = r"\s+$" # ^\s+$ remove only trailing spaces # dollar ($) matches spaces only at the end of the string
replacement = ""
result_str = re.sub(pattern_to_replace,replacement,target_string)
print(result_str)

#--Remove Remove both leading and trailing spaces. (pattern to remove  ^\s+|\s+$ )
target_string = "   Jessa Knows Testing And Machine Learning.   \t\n"
pattern_to_replace = r"^\s+|\s+$" # ^\s+ remove leading spaces # ^\s+$ removes trailing spaces # | operator to combine both patterns
replacement = ""
result_str = re.sub(pattern_to_replace,replacement,target_string)
print(result_str)