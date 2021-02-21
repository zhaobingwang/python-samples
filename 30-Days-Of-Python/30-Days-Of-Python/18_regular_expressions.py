print('---------- The re Module ----------')
import re

# To find a pattern we use different set of re character sets that allows to search for a match in a string.
print('\t---------- Match ----------')
txt = 'I\'m learning Python'
# It returns an object with span, and match
match = re.match('I\'m learning', txt, re.I)
print(match)  # <re.Match object; span=(0, 12), match="I'm learning">
# We can get the starting and ending position of the match as tuple using span
span = match.span()  # (0, 12)
print(span)
start, end = span
print(start, end)  # 0 12
substring = txt[start:end]
print(substring)  # I'm learning

print('\t---------- Search ----------')
txt = '''Don't forget, a person's greatest emotional need is to feel appreciated.'''
match = re.search('forget', txt, re.I)
print(match)  # <re.Match object; span=(6, 12), match='forget'>

span = match.span()
print(span)  # (6, 12)
start, end = span
print(start, end)  # 6 12
substring = txt[start:end]
print(substring)  # forget

print('\t---------- Searching for All Matches Using findall ----------')
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

print('\t---------- Replacing a Substring ----------')
match_replaced = re.sub('Python|python', 'Java', txt, re.I)
print(match_replaced)

match_replaced = re.sub('[Pp]ython', 'Java', txt, re.I)
print(match_replaced)

print('---------- Splitting Text Using RegEx Split ----------')
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# ['Python is the most beautiful language that a human being has ever created',
# '\nI recommend python for a first programming language']
print(re.split('\.', txt))

print('---------- Writing RegEx Patterns ----------')
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']
# 添加flag re.I 使大小写敏感
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# 使用字符集匹配
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
