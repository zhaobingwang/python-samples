letter = 'python'
print(letter)
print(len(letter))

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
print('##### String Concatenation #####')
first_name = 'San'
last_name = 'Zhang'
space = ' '
full_name = last_name + space + first_name
print(full_name)

# Escape Sequences in Strings
print('##### Escape Sequences in Strings #####')
print('a\nb')
print('c\td')
print('\\')
print('\'')
print('\"')

# String formatting
print('##### String formatting #####')
print('%s %s' % (last_name, first_name))  # %s - String (or any object with a string representation, like numbers)
print('%d' % 1)  # %d - Integers
print('%f' % 1.23)  # %f - Floating point numbers
print('%.2f' % 1.234)  # %.f - Floating point numbers with fixed precision

print('\t----- New Style String Formatting (str.format) In Python3 -----')

print('{} {}'.format(last_name, first_name))
print('{:.2f}'.format(1.234))
print('{:d}'.format(1))
print('{:f}'.format(1.23))

print('\t----- String Interpolation / f-Strings (Python 3.6+) -----')
a = 1
b = 2
print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b:.2f}')

print('\t----- Python Strings as Sequences of Characters -----')
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

print('\t----- Accessing Characters in Strings by Index -----')
print(language[0])
lastIndex = len(language) - 1
print(language[lastIndex])
print(language[-1])  # start from right

print('\t----- Slicing Python Strings -----')
first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
print(first_three)
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

print('\t----- Reversing a String -----')
print(language[::-1])  # nohtyP

print('\t----- Skipping Characters While Slicing -----')
print(language[0:6:2])  # Pto

print('\t----- String Methods -----')

challenge = 'thirty days of python'

# capitalize(): Converts the first character of the string to capital Letter
print(challenge.capitalize())  # 'Thirty days of python'
# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count('o'))  # 2
print(challenge.count('y', 8, 17))  # 2
print(challenge.count('days'))  # 1
# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('python'))  # True
print(challenge.endswith('on'))  # True
print(challenge.endswith('aon'))  # False
# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(20))
# find(): Returns the lowest index of the first occurrence of a substring, if not found returns -1
print(challenge.find('y'))  # 5
print(challenge.find('x'))  # -1
# rfind(): Returns the highest index of the first occurrence of a substring, if not found returns -1
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th'))  # 17
print(challenge.rfind('x'))  # -1

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index
# (default 0 and string length - 1)
challenge = 'thirty days of python'
print(challenge.index('of'))  # 12
print(challenge.index('of', 10))  # 12

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index
# (default 0 and string length - 1)
print(challenge.rindex('o'))  # 19
print(challenge.rindex('o', 10))  # 19

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True
challenge = 'thirty days of python'
print(challenge.isalnum())  # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
print(challenge.isalpha())  # False
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())  # True

# isdecimal(): Checks if all characters in a string are decimal (0-9)
print(challenge.isdecimal())  # False
challenge = '100'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdecimal())  # False
challenge = '1 2'
print(challenge.isdecimal())  # False

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print(challenge.isdigit())  # False
challenge = '12'
print(challenge.isdigit())  # True
challenge = '\u00B2'
print(challenge.isdigit())  # True
# isnumeric(): Checks if all characters in a string are numbers or number related
# (just like isdigit(), just accepts more symbols, like ½)
challenge = '12'
print(challenge.isnumeric())  # True
challenge = '\u00B2'
print(challenge.isnumeric())  # True
challenge = '1.2'
print(challenge.isnumeric())  # False
# isidentifier(): Checks for a valid identifier - means it checks, if a string is a valid variable name
challenge = 'name'
print(challenge.isidentifier())  # True
challenge = '1name'
print(challenge.isidentifier())  # False
challenge = 'first name'
print(challenge.isidentifier())  # False

# islower(): Checks if all alphabet characters in the string are lowercase
print(challenge.islower())  # True
challenge = 'First name'
print(challenge.islower())  # False

# isupper(): Checks if all alphabet characters in the string are uppercase
print(challenge.isupper())  # False
challenge = 'NAME'
print(challenge.isupper())  # True

# join(): Returns a concatenated string
tags = ['friendly', 'humorous', 'sapient']
print('|'.join(tags))

# strip(): Removes all given characters starting from the beggining and end of the string
challenge = ' hello python'
print(challenge.strip())  # result: hello python
print(challenge.strip('on'))  # result:hello pyth

# replace(): Replaces substring with a given string
challenge = 'Hello,Python.'
print(challenge.replace('Python', 'C#'))

# split(): Splits the string, using given string as a separator
challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', '))  # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
print(challenge.startswith('x'))  # False
