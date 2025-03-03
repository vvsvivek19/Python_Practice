#All email addresses:
text = "Contact me at user@example.com or admin@site.org"
digit = re.findall(r"[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
print(digit)