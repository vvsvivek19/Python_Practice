import re
match = re.search('iig','called piiig')
print(match)
print(match.group())
match = re.search('iigs','called piiig')
print(match)

def Find(pat,text):
    match = re.search(pat,text)
    if match:
        print(match.group())
    else:
        print("Not Found!")

Find('ig','called piiig')

"""
. (dot) any character
\w word char - letter, digit, underscore
\d digit
\s whitespace  \S non-whitespace
+ 1 or more
* 0 or more
"""
Find('...g','called piiig')
Find('x...g','called piiig') #for a pattern to match, 100% should match. 
Find('..g','called piiig   much better:xyzg')
Find('x..g','called piiig   much better:xyzg')
Find(r'c\.l','c.lled piiig   much better:xyzg')
Find(r':\w\w\w','blah :cat blah blah')
Find(r':\d\d\d','blah :cat :123xxx blah blah')
Find(r'\d\s\d\s\d','1 2 3')
Find(r'\d\s+\d\s+\d','1    2               3')
Find(r':\w+','blah blah :kitten :123xxx blah blah')
Find(r':\d+','blah blah :kitten :123xxx blah blah') #only searches for a complete pattern consisting of : and digit
Find(r':\d+','blah blah :kitten :123 xxx blah blah')
Find(r':.+','blah blah :kitten :123 xxx blah blah')
Find(r':\S+','blah blah :kitten123xxx@#ayattasne blah blah')
Find(r'\w+@\w+','blah blah nick.p@gmail.com yatta @')
Find(r'[\w.]+@[\w.]+','blah blah nick.p@gmail.com yatta @')
Find(r'\w[\w.]*@[\w.]+','blah blah nick.p@gmail.com yatta @') #email must start with a word character
m = re.search(r'([\w.]+)@([\w.]+)','blah blah nick.p@gmail.com yatta @')
print(m.group())
print(m.group(1))
print(m.group(2))
m = re.findall(r'[\w.]+@[\w.]+','blah blah nick.p@gmail.com yatta foo@bar')
print(m)
m = re.findall(r'([\w.]+)@([\w.]+)','blah blah nick.p@gmail.com yatta foo@bar')
print(m)