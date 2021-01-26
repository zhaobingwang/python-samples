# Built in functions
print(max(10, 20, 30))
print(min(10, 20, 30))


# Variables
first_name = 'San'
last_name = 'Zhang'
country = 'China'
city = 'Hangzhou'
age = 20
tags = ['runner', 'geek', 'mountaineer']
person_info = {
    'name': 'Zhang San',
    'age': 20,
    'country': 'China',
    'city': 'Hangzhou'
}

print(last_name)
print(person_info)
print(person_info.get('name'))

# first_name = input('What is your name: ')
# age = input('How old are you? ')
# print(first_name)
# print(age)


# Data Type Conversion

num_int = 10
num_float = float(num_int)
str_int = str(num_int)
to_list = list(str_int)
print('num_int: ', num_int)
print('num_float: ', num_float)
print('str_int: ', str_int)
print('to_list: ', to_list)  # Result: ['1', '0']
