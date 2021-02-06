print('---------- Function as a Parameter ----------')

print('\t---------- Function as a Parameter ----------')


def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, *args):
    summation = f(*args)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15

print('\t---------- Function as a Return Value ----------')


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))

print('----------  Python Closures ----------')


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(1))  # 11

print('----------  Python Decorators ----------')

print('\t---------- Creating Decorators ----------')


def do_something():
    return 'Python Learning'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


result = uppercase_decorator(do_something)
print(result())


@uppercase_decorator
def do_something2():
    return 'Python Learning'


print(do_something2())

print('\t---------- Applying Multiple Decorators to a Single Function ----------')


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string_decorator(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string

    return wrapper


@split_string_decorator
@uppercase_decorator
def do_something3():
    return 'Python Learning'


print(do_something3())

print('\t---------- Accepting Parameters in Decorator Functions ----------')


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print('I live in {}'.format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print('I am {} {}'.format(first_name, last_name, country))


print_full_name('San', 'Zhang', 'China')

print('---------- Built-in Higher Order Functions ----------')

print('\t---------- Map Function ----------')
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['Zhang San', 'Li Si', 'Wang Wu']


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# use lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

print('\t---------- Filter Function ----------')

numbers = [1, 2, 3, 4, 5]


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))

names = ['Zhang San', 'Li Si', 'Wang Wu']


def is_name_long(name):
    if len(name) > 5:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))

print('\t---------- Reduce Function ----------')
import functools

numbers = [1, 2, 3, 4, 5]


def add_two_nums(x, y):
    return x + y


total = functools.reduce(add_two_nums, numbers)
print(total)
