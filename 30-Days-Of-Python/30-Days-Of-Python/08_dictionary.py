print('---------- Creating a Dictionary ----------')
empty_dict = {}
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
print(dic)
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
print('---------- Dictionary Length ----------')
print(len(person))

print('---------- Accessing Dictionary Items ----------')
print(person['name'])
print(person['age'])
print(person['skills'])
print(person.get('city'))  # None

print('---------- Adding Items to a Dictionary ----------')
person['title'] = 'Engineer'
person['skills'].append('SQL')
print(person)

print('---------- Modifying Items in a Dictionary ----------')
person['age'] = 25
print(person.get('age'))

print('---------- Checking Keys in a Dictionary ----------')
print('name' in person)

print('---------- Removing Key and Value Pairs from a Dictionary ----------')
# pop(key): removes the item with the specified key name
person.pop('age')
print(person.get('age'))  # None

# popitem(): removes the last item
person.popitem()
print(person.get('title'))  # None

# del: removes an item with specified key name
del person['is_married']
print(person.get('is_married'))  # None

print('---------- Changing Dictionary to a List of Items ----------')
# The items() method changes dictionary to a list of tuples.
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
print(dic)
print(dic.items())

print('---------- Clearing a Dictionary ----------')
print(dic.clear())  # None

print('---------- Deleting a Dictionary ----------')
del dic

print('---------- Copy a Dictionary ----------')
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
dic_copy = dic.copy()
print(dic_copy)

print('---------- Getting Dictionary Keys as a List ----------')
keys = dic.keys()
print(keys)

print('---------- Getting Dictionary Values as a List ----------')
values = dic.values()
print(values)
