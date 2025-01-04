text = """Beautiful is better than ugly 
Explicit is better than implicit Simple is 
better than complex Complex is better than complicated """.lower()
unique_words = set()
for words in text.split():
    unique_words.add(words)
print(unique_words)