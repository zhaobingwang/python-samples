import my_module

print('---------- Importing a Module ----------')
print(my_module.generate_full_name('San', 'Zhang'))

print('---------- Import Functions from a Module ----------')
from my_module import generate_full_name

print(generate_full_name('San', 'Zhang'))

print('---------- Import Functions from a Module and Renaming ----------')
from my_module import generate_full_name as fullname

print(fullname('San', 'Zhang'))

print('---------- Import Built-in Modules ----------')

print('\t---------- OS Module ----------')
import os

# Creating a directory
# os.mkdir('2021-02-05')

# Getting current working directory
print(os.getcwd())

# Changing the current directory
os.chdir('../')

# Removing directory
# os.rmdir('2021-02-05')

print('\t---------- Sys Module ----------')
import sys

# run python script.py Asabeneh 30DaysOfPython in command
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# to exit sys
# sys.exit()
# To know the largest integer variable it takes
print(sys.maxsize)

# To know environment path
print(sys.path)

# To know the version of python you are using
print(sys.version)

print('\t---------- Statistics Module ----------')
# 更多关于statistics的信息参见：https://docs.python.org/zh-cn/3.9/library/statistics.html
from statistics import *  # importing all the statistics modules

ages = [22, 25, 23, 23, 29, 35, 27, 26, 43, 28, 25, 32, 25, 31, 25]
print(mean(ages))  # 平均数
print(median(ages))  # 中位数
print(mode(ages))  # most common value(最常见的值)
print(stdev(ages))  # 数据的样本标准差

print('\t---------- Math Module ----------')
import math

print(math.pi)
print(math.sqrt(9))  # math.sqrt(x): 返回x的平方根
print(math.pow(2, 3))  # math.pow(x,y): 将返回 x 的 y 次幂
print(math.floor(3.14))  # math.floor(x): 返回 x 的向下取整，小于或等于 x 的最大整数
print(math.ceil(3.14))  # math.ceil(x): 返回 x 的上限，即大于或者等于 x 的最小整数
print(math.log10(100))  # 返回 x 底为10的对数。这通常比 log(x, 10) 更准确

# Import multiple functions at once
from math import pi, sqrt

print(pi)
print(sqrt(36))

# Import all the function in math module we can use * .
from math import *

print(pi)
# Rename the name of the function.
from math import pi as PI

print(PI)

print('\t---------- String Module ----------')
import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print('\t---------- Random Module ----------')
from random import random, randint

print(random())  # it returns a random number between 0 and 0.9999...
print(randint(1, 10))  # it returns a random integer number in [1,10]
