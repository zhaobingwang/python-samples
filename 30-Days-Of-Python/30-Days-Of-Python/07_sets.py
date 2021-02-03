print('---------- Creating a Set ----------')
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

print('---------- Getting Set\'s Length ----------')
print(len(fruits))

print('---------- Accessing Items in a Set ----------')
print('orange' in fruits)
print('apple' in fruits)

print('---------- Adding Items to a Set ----------')
fruits.add('apple')
print(fruits)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

print('---------- Removing Items from a Set ----------')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits)

print('---------- Clearing Items in a Set ----------')
fruits.clear()
print(fruits)

print('---------- Deleting a Set ----------')
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

print('---------- Converting List to Set ----------')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = set(fruits)
print(fruits)

print('---------- Joining Sets ----------')
print('\t---------- union(): This method returns a new set ----------')
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))
print(fruits)
print(vegetables)
print('\t---------- update(): This method inserts a set into a given set ----------')
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)  # {'mango', 'orange', 'banana', 'lemon', 'cabbage', 'potato', 'tomato', 'carrot', 'onion'}
print(vegetables)  # {'carrot', 'cabbage', 'potato', 'tomato', 'onion'}

print('---------- Finding Intersection Items ----------')
# Intersection returns a set of items which are in both the sets.
py = {'P', 'y', 't', 'h', 'o', 'n'}
js = {'J', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't'}
print(py.intersection(js))  # t

print('---------- Checking Subset and Super Set ----------')
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issuperset(even_numbers))  # True
print(whole_numbers.issubset(even_numbers))  # False
print(even_numbers.issubset(whole_numbers))  # True
print(even_numbers.issuperset(whole_numbers))  # False

print('---------- Checking the Difference Between Two Sets ----------')
# difference(): returns the difference between two sets.
print(whole_numbers.difference(even_numbers))  # {1, 3, 5, 7, 9}

print('---------- Finding Symmetric Difference Between Two Sets ----------')
# 对称差：两个相对补集的并集
# It returns the the symmetric difference between two sets.
# It means that it returns a set that contains all items from both sets,
# except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5, 11}
print(whole_numbers.symmetric_difference(some_numbers))  # {0, 6, 7, 8, 9, 10, 11}

print('---------- Checking disjoint Sets ----------')
# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True
