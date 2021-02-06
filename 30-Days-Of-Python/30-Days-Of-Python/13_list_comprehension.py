print('---------- List Comprehension ----------')
print('\t---------- Example:1 ----------')

language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

print('\t---------- Example:2 ----------')
numbers = [i for i in range(11)]  # To generate numbers from 0 to 10
print(numbers)

square = [i * i for i in range(11)]  # Do mathematical operations during iteration
print(square)

numbers = [(i, i * i) for i in range(11)]  # to make a list of tuples
print(numbers)

print('\t---------- Example:3 ----------')

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#  Filter numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i > 0 and i % 2 == 0]
print(positive_even_numbers)  # [4, 6, 8, 10]

# Flattening a three dimensional array
three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in three_dimen_list for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('---------- Lambda Function ----------')
print('\t---------- Creating a Lambda Function ----------')
add_two_nums = lambda a, b: a + b
print(add_two_nums(1, 2))
# Self invoking lambda function
print((lambda a, b: a + b)(1, 2))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(2, 3, 4))

print('\t---------- Lambda Function Inside Another Function ----------')


def power(x):
    return lambda n: x ** n


cube = power(2)(3)
print(cube)  # 8
