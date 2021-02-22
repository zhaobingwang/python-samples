print('---------- Opening Files for Reading ----------')
f = open('./files/reading_file_example.txt')
print(f)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='cp936'>

print('\t---------- read() ----------')
# read(): read the whole text as string. If we want to limit the number of characters we read,
# we can limit it by passing int value to the methods.

f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))  # <class 'str'>
print(txt)  # Hello,Python!
f.close()

f = open('./files/reading_file_example.txt')
txt = f.read(5)
print(type(txt))  # <class 'str'>
print(txt)  # Hello
f.close()

print('\t---------- readline(): read only the first line ----------')
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))  # <class 'str'>
print(line)  # Hello,Python!
f.close()

print('\t---------- readlines(): read all the text line by line and returns a list of lines ----------')
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))  # <class 'list'>
print(lines)  # ['Hello,Python!']
f.close()

print('\t---------- splitlines() ----------')
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))  # <class 'list'>
print(lines)  # ['Hello,Python!']
f.close()

print('\t---------- Another way to close a file ----------')
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))  # <class 'list'>
    print(lines)  # ['Hello,Python!']

print('---------- Opening Files for Writing and Updating ----------')
# To write to an existing file, we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not exist it raise FileNotFoundError.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.
with open('./files/writing_file_example.txt', 'a') as f:
    f.write('Hello,Python!')
with open('./files/writing_file_example.txt', 'w') as f:
    f.write('Hello,Java!')

print('---------- Deleting Files ----------')
import os

if os.path.exists('./files/writing_file_example.txt'):
    os.remove('./files/writing_file_example.txt')
else:
    os.remove('The file does not exist!')

print('---------- File Types ----------')

print('\t---------- File with json Extension ----------')
# dictionary
person_dct = {
    "name": "Zhang San",
    "country": "China",
    "city": "Hangzhou",
    "skills": ["Java", "C#", "Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Zhang San', 'country': 'China', 'city': 'Hangzhou', 'skills': ['Java', 'C#', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Zhang San",
    "country":"China",
    "city":"Hangzhou",
    "skills":["Java", "C#","Python"]
}'''

print('\t---------- Changing JSON to Dictionary ----------')
import json

person_json = '''{
    "name":"Zhang San",
    "country":"China",
    "city":"Hangzhou",
    "skills":["Java", "C#","Python"]
}'''
person_dct = json.loads(person_json)
print(person_dct)
print(person_dct['name'])

print('\t---------- Changing Dictionary to JSON ----------')
person_dct = {
    "name": "Zhang San",
    "country": "China",
    "city": "Hangzhou",
    "skills": ["Java", "C#", "Python"]
}
person_json = json.dumps(person_dct, indent=4)  # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))  # <class 'str'>
print(person_json)

print('\t---------- Saving as JSON File ----------')
person_dct = {
    "name": "Zhang San",
    "country": "China",
    "city": "Hangzhou",
    "skills": ["Java", "C#", "Python"]
}

with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person_dct, f, ensure_ascii=False, indent=4)

print('\t---------- File with csv Extension ----------')
import csv
# with open('./files/csv_example.csv') as f:
