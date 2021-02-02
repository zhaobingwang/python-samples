# Creating a Tuple
print('---------- Creating a Tuple ----------')
tpl = ('item1', 'item2', 'item3')
print(tpl)
# Tuple length
print('---------- Tuple length ----------')
print(len(tpl))

# Accessing Tuple Items
tpl = ('item1', 'item2', 'item3')
print('---------- Accessing Tuple Items ----------')
print('\t---------- Positive Indexing ----------')
print(tpl[0])
print('\t---------- Positive Indexing ----------')
print(tpl[-3])
print(tpl[-1])

# Slicing tuples
print('---------- Slicing tuples ----------')
print('\t---------- Range of Positive Indexes ----------')
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
print(all_fruits)
orange_mango = fruits[1:3]
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

print('\t---------- Range of Negative Indexes ----------')
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]  # all items
print(all_fruits)
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
print(orange_mango)
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

# Changing Tuples to Lists
print('---------- Changing Tuples to Lists ----------')
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
print('---------- Checking an Item in a Tuple ----------')
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # True
print('apple' in fruits)  # False
# fruits[0] = 'apple'  # TypeError: 'tuple' object does not support item assignment

print('---------- Joining Tuples ----------')
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print('---------- Deleting Tuples ----------')
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
