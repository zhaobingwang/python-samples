print('---------- While Loop ----------')
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

print('---------- Break and Continue Part1 ----------')
print('\t---------- Part1 ----------')
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
print('\t---------- Part2 ----------')
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

print('---------- For Loop ----------')
print('\t---------- For loop with list ----------')
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

print('\t---------- For loop with string ----------')
language = 'Python'
for letter in language:
    print(letter)

print('\t---------- For loop with tuple ----------')
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print('\t---------- For loop with dictionary ----------')
# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'name': 'ZhangSan',
    'age': 22,
    'country': 'China',
    'is_married': False,
    'skills': ['JavaScript', 'VUE', 'Go', 'Java', 'C#', 'Python'],
    'address': {
        'street': 'WanTang Road',
        'zipcode': '310000'
    }
}
print('\t\t----- K -----')
for key in person:
    print(key)
print('\t\t----- KV -----')
for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

print('\t---------- For loop with set ----------')
it_companies = {'Microsoft', 'Apple', 'Alibaba', 'Tencent'}
for company in it_companies:
    print(company)

print('---------- Break and Continue Part2 ----------')
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

print('\t----------')
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print('loop\'s end')

print('outside the loop')

print('---------- The Range Function ----------')
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # 2 arguments indicate start and end of the sequence, step set to default 1
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # {0, 2, 4, 6, 8, 10}

for number in range(5):
    print(number)

print('---------- Nested For Loop ----------')
person = {
    'name': 'ZhangSan',
    'age': 22,
    'country': 'China',
    'is_married': False,
    'skills': ['JavaScript', 'VUE', 'Go', 'Java', 'C#', 'Python'],
    'address': {
        'street': 'WanTang Road',
        'zipcode': '310000'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

print('---------- For Else ----------')
for number in range(5):
    print(number)
else:
    print('The loop stops at', number)

print('---------- Pass ----------')
# In python when statement is required (after semicolon), but we don't like to execute any code there,
# we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(5):
    pass
else:
    print('The loop stops at', number)
