print('---------- Function without Parameters ----------')


def add_two_numbers():
    num_1 = 1
    num_2 = 2
    total = num_1 + num_2
    print(total)


add_two_numbers()

print('---------- Function Returning a Value Part 1 ----------')


def add_two_numbers():
    num_1 = 1
    num_2 = 2
    total = num_1 + num_2
    return total


print(add_two_numbers())

print('---------- Function with Parameters ----------')


def greeting(name):
    return 'Hi,' + name


print(greeting('ZhangSan'))


def sum_two(num1, num2):
    total = num1 + num2
    return total


print(sum_two(1, 3))

print('---------- Passing Arguments with Key and Value ----------')


def sub_two(num1, num2):
    total = num1 - num2
    print(total)


sub_two(num2=5, num1=3)  # -2

print('---------- Function Returning a Value Part 2 ----------')

print('\t---------- Returning a string ----------')


def get_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name


print(get_full_name('San', 'Zhang'))

print('\t---------- Returning a numbers ----------')


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print(calculate_age(2021, 2000))

print('\t---------- Returning a boolean ----------')


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(6))  # True
print(is_even(5))  # False

print('\t---------- Returning a list ----------')


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))

print('---------- Function with Default Parameters ----------')


def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age


print(calculate_age(2000))

print('---------- Arbitrary Number of Arguments ----------')


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(1, 2, 3, 4, 5))

print('---------- Default and Arbitrary Number of Parameters in Functions ----------')


def generate_groups(team, *args):
    print(team + ':')
    for i in args:
        print('  ', i)


generate_groups('Team-1', 'Zhang San', 'Li Si', 'Wang Wu')

print('---------- Function as a Parameter of Another Function ----------')


def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))
