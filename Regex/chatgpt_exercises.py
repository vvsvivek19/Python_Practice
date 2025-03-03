import re

#Beginner Level

text = "Order ID: 12345, Amount: $99"
all_digits = re.findall(r"\d+",text)
print(all_digits)

text = "Apple and apricot are amazing."
all_names_with_A = re.findall(r"a\w+",text,re.IGNORECASE)
print(all_names_with_A)

text = "Hello world"
upper = re.match(r"^[A-Z]",text)
print(bool(upper))

text = "hello world"
upper = re.match(r"^[A-Z]",text)
print(bool(upper))

text = "These words: apple; mango, happy, smile, banana"
five_letters = re.findall(r"\b\w{5}\b",text)
print(five_letters)

text = "Order #123, Price: $45.67"
all_digits = re.findall(r"\d+",text)
print(all_digits)

#Find all words that start with a capital letter in a sentence.
text = "Hello there, John! How are You?"
capital = re.findall(r"\b[A-Z]\w+\b",text)
print(capital)

#Extract all words that contain only lowercase letters.
text = "hello World this is regex"
lower = re.findall(r"\b[a-z]+\b",text)
print(lower)

#Find all words that contain at least one digit.
text = "user1, pass123, test, 4fun"
digit = re.findall(r"\b\d\w+\b|\b\w+\d\b",text)
print(digit)

#All email addresses:
text = "Contact me at user@example.com or admin@site.org"
digit = re.findall(r"[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
print(digit)


#Intermediate Exercise
text = "Contact us at support@email.com or admin@site.org"
addresses = re.findall(r"[\w.]+@[\w.]+",text)
#addresses = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(addresses)

text = "My number is 987-654-3210"
phone = re.findall(r"[\d.-]+",text)
print(bool(phone))

text = "My number is 987-654-3210"
phone = re.findall(r"[\d-]+",text)
#phone = re.findall(r"\b\d{3}-\d{3}-\d{4}\b", text)
print(bool(phone))

text = "Python is fun"
res_text = re.sub(r"\s","_",text)
print(res_text)

text = "Today's date is 03/03/2025 and yesterday was 02-03-2025"
dates = re.findall(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",text)

print(dates)

#Advance Exercises
tweet = "Loving the #Python #Regex challenge! #coding"
hastags = re.findall(r'#\w+',tweet)
print(hastags)

url = "Visit https://www.google.com and http://example.org"
domain = re.findall(r"https?://(?:www.)?([\w.-]+)",url)
print(domain)

def validate_password(password):
    validation = re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$",password)
    return bool(validation)

print(validate_password("MyPassword@123"))
print(validate_password("weakpass"))

text =  "The server IPs are 192.168.1.1 and 256.300.999.1"
ip_address = re.findall(r"\b(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b",text)
print(ip_address)

