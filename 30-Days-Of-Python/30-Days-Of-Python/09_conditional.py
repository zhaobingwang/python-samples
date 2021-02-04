print('---------- If Condition ----------')
a = 1
if a > 0:
    print('A is a positive number')

print('---------- If Else ----------')
a = -1
if a > 0:
    print('A is a positive number')
else:
    print('A is a negative number')

print('---------- If Elif Else ----------')
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

print('---------- Short Hand ----------')
a = 1
print('A is positive') if a > 0 else print('A is negative')  # first condition met, 'A is positive' will be printed

print('---------- Nested Conditions ----------')
a = 3
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

print('---------- If Condition and Logical Operators ---------')
a = 2
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

print('---------- If and Or Logical Operators ---------')
user = 'ZhangSan'
access_level = 1
if user == 'admin' or access_level >= 9:
    print('Access granted!')
else:
    print('Access denied!')
