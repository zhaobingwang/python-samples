print('---------- Create List ----------')
empty_lst = list()
print(len(empty_lst))
empty_lst = []
print(len(empty_lst))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print(len(fruits))

# Lists can have items of different data types
lst = ['Zhang San', 22, True, {'country': 'China', 'city': 'Hangzhou'}]
print(lst)

print('---------- Accessing List ----------')

# Accessing List Items Using Positive Indexing
print('\t---------- Positive Indexing ----------')
print(fruits[0])
last_index = len(fruits) - 1;
print(fruits[last_index])

# Accessing List Items Using Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
print('\t---------- Negative Indexing ----------')
print(fruits[-1])
print(fruits[-2])
print(fruits[-4])

print('---------- Unpacking List Items ----------')
lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']

# First Example
print('\t---------- First Example----------')
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)  # banana
print(second_fruit)  # orange
print(third_fruit)  # mango
print(rest)  # ['lemon','lime','apple']

# Second Example about unpacking list
print('\t---------- Second Example----------')
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10
# Third Example about unpacking list
print('\t---------- Third Example----------')
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

print('---------- Slicing Items from a List ----------')
print('\t---------- Positive Indexing ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[1:3]  # it does not include the first index
print(orange_and_mango)  # ['orange', 'mango']
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)
orange_and_lemon = fruits[::2]  # here we used a 3rd argument, step. It will take every 2cnd item - ['orange', 'lemon']
print(orange_and_lemon)
print('\t---------- Negative Indexing ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
print(all_fruits)
orange_and_mango = fruits[-3:-1]  # it does not include the last index
print(orange_and_mango)
orange_mango_lemon = fruits[-3:]  # this will give the same result as the one above
print(orange_mango_lemon)
reverse_fruits = fruits[::-1]  # a negative step will take the list in reverse order
print(reverse_fruits)

print('---------- Modifying Lists ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'I am changed'
print(fruits)

print('---------- Checking Items in a List ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
print('orange' in fruits)
print('orang' in fruits)

print('---------- Adding Items to a List ----------')
fruits.append('apple')
print(fruits)

print('---------- Inserting Items into a List ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(0, 'apple')
print(fruits)
fruits.insert(2, 'pear')
print(fruits)

print('---------- Removing Items from a List ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)

print('---------- Removing Items Using Pop ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)  # ['orange', 'mango']

print('---------- Removing Items Using Del ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)

print('---------- Clearing List Items ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear();
print(fruits)

print('---------- Copying a List ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

print('---------- Joining Lists ----------')
print('\t---------- Plus Operator (+) ----------')
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print('\t---------- Joining using extend() method ----------')
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)

print('---------- Counting Items in a List ----------')
# The count() method returns the number of times an item appears in a list
num = [1, 2, 3, 4, 5, 3, 2, 9, 4]
print(num.count(3))

print('---------- Finding Index of an Item ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))

print('---------- Reversing a List ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

print('---------- Sorting List Items ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
# sort(): this method modifies the original list
print('\t---------- sort() ----------')
fruits.sort()  # ascending
print(fruits)
fruits.sort(reverse=True)  # descending
print(fruits)
# sorted(): returns the ordered list without modifying the original
print('\t---------- sorted() ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print(sorted(fruits))
print(sorted(fruits, reverse=True))
