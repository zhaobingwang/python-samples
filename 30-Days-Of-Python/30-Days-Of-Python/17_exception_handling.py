print('---------- Exception Handling ----------')

try:
    r = 10 / 0
except ZeroDivisionError as e:
    print(e)  # division by zero
finally:
    print('Always Run')

print('---------- Packing and Unpacking Arguments in Python ----------')

print('\t---------- Unpacking ----------')

# Unpacking Lists
print('----------')


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


try:
    lst = [1, 2, 3, 4, 5]
    print(sum_of_five_nums(lst))
except BaseException as e:
    print(e)  # sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

try:
    lst = [1, 2, 3, 4, 5]
    print(sum_of_five_nums(*lst))  # 15
except BaseException as e:
    print(e)

#  use unpacking in the range built-in function
numbers = range(1, 6)
print(list(numbers))  # [1, 2, 3, 4, 5]
args = [1, 6]
numbers = range(*args)
print(list(numbers))  # [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7
one, two, *rest = numbers
print(one, two, rest)  # 1 2 [3, 4, 5, 6, 7]

# Unpacking Dictionaries
print('------------------')


def unpacking_person_info(name, age, country, city):
    return f'{name} lives in {country},{city}.He is {age} years old.'


dct = {'name': 'Zhang San', 'age': 25, 'country': 'China', 'city': 'Hangzhou'}
print(unpacking_person_info(**dct))

print('---------- Packing ----------')
print('\t------------ Packing Lists ----------')


def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

print('\t------------ Packing Dictionaries ----------')


def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs


print(packing_person_info(name='Zhang San', age=25, country='China'))
# name = Zhang San
# age = 25
# country = China
# {'name': 'Zhang San', 'age': 25, 'country': 'China'}


print('---------- Spreading ----------')
lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
lst = [0, *lst_one, *lst_two]
print(lst)

print('---------- Enumerate ----------')
cities = ['Beijing', 'Shanghai', 'Shenzhen', 'Hangzhou']
for index, city in enumerate(cities):
    if city == 'Hangzhou':
        print(f'The city {city} has been found at index {index}')

print('---------- Zip ----------')

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'},
# {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}]
print(fruits_and_veges)
