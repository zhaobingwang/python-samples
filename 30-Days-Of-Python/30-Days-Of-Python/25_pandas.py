print('---------- Pandas ----------')
import pandas as pd
import numpy as np

print('---------- Creating Pandas Series with Default Index ----------')
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

print('---------- Creating Pandas Series with custom index ----------')
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Apple', 'Banana', 'Orange']
fruits = pd.Series(fruits, index=[11, 12, 13])
print(fruits)

print('---------- Creating Pandas Series from a Dictionary ----------')
dct = {'name': 'Zhang San', 'country': 'China', 'city': 'Hangzhou'}
s = pd.Series(dct)
print(s)

print('---------- Creating a Constant Pandas Series ----------')
s = pd.Series(10, index=[1, 2, 3])
print(s)
# output:
# 1    10
# 2    10
# 3    10
# dtype: int64

print('---------- Creating a Pandas Series Using Linspace ----------')
s = pd.Series(np.linspace(10, 20, 3))  # 最后这个3表示等分为3组数据
print(s)
# output:
# 0    10.0
# 1    15.0
# 2    20.0
# dtype: float64


print('---------- DataFrames ----------')
print('---------- Creating DataFrames from List of Lists ----------')
data = [
    ['Zhang San', 'China', 'Hangzhou'],
    ['Li Si', 'China', 'Shanghai'],
    ['Jack', 'American', 'Washington']
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
print(df)
# result:
#        Names   Country        City
# 0  Zhang San     China    Hangzhou
# 1      Li Si     China    Shanghai
# 2       Jack  American  Washington


print('---------- Creating DataFrame Using Dictionary ----------')
data = {
    'Name': ['Zhang San', 'Li Si', 'Jack'],
    'Country': ['China', 'China', 'American'],
    'City': ['Hangzhou', 'Shanghai', 'Washington']
}
df = pd.DataFrame(data)
print(df)
# result:
#         Name   Country        City
# 0  Zhang San     China    Hangzhou
# 1      Li Si     China    Shanghai
# 2       Jack  American  Washington


print('---------- Creating DataFrames from a List of Dictionaries ----------')
data = [
    {'Name': 'Zhang San', 'Country': 'China', 'City': 'Hangzhou'},
    {'Name': 'Li Si', 'Country': 'China', 'City': 'Shanghai'},
    {'Name': 'Jack', 'Country': 'American', 'City': 'Washington'}
]
df = pd.DataFrame(data)
print(df)
# result:
#         Name   Country        City
# 0  Zhang San     China    Hangzhou
# 1      Li Si     China    Shanghai
# 2       Jack  American  Washington


print('---------- Reading CSV File Using Pandas ----------')
df = pd.read_csv('./files/weight-height.csv')
print(df)
# output:
#       Gender     Height      Weight
# 0       Male  73.847017  241.893563
# 1       Male  68.781904  162.310473
# 2       Male  74.110105  212.740856
# 3       Male  71.730978  220.042470
# 4       Male  69.881796  206.349801
# ...      ...        ...         ...
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103
#
# [10000 rows x 3 columns]

print('---------- Data Exploration ----------')

# 获取前5行
print(df.head())  # give five rows we can increase the number of rows by passing argument to the head() method
# output:
#   Gender     Height      Weight
# 0   Male  73.847017  241.893563
# 1   Male  68.781904  162.310473
# 2   Male  74.110105  212.740856
# 3   Male  71.730978  220.042470
# 4   Male  69.881796  206.349801

print(df.head(3))
# output
#   Gender     Height      Weight
# 0   Male  73.847017  241.893563
# 1   Male  68.781904  162.310473
# 2   Male  74.110105  212.740856

# 10000行，3列
print(df.shape)  # output: (10000, 3)

# 获取行
print(df.columns)  # output: Index(['Gender', 'Height', 'Weight'], dtype='object')

# 获取最后5行
print(df.tail())  # tails give the last five rows, we can increase the rows by passing argument to tail method
# output
#       Gender     Height      Weight
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

# 获取最后3行
print(df.tail(3))
# output
#       Gender     Height      Weight
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

# 获取指定列
heights = df['Height']
print(heights)
# output
# 0       73.847017
# 1       68.781904
# 2       74.110105
# 3       71.730978
# 4       69.881796
#           ...
# 9995    66.172652
# 9996    67.067155
# 9997    63.867992
# 9998    69.034243
# 9999    61.944246
# Name: Height, Length: 10000, dtype: float64

# 获取height统计数据
print(heights.describe())
# output
# count    10000.000000
# mean        66.367560
# std          3.847528
# min         54.263133
# 25%         63.505620
# 50%         66.318070
# 75%         69.174262
# max         78.998742
# Name: Height, dtype: float64

# 获取dataFrame的统计数据
print(df.describe())
# output
#              Height        Weight
# count  10000.000000  10000.000000
# mean      66.367560    161.440357
# std        3.847528     32.108439
# min       54.263133     64.700127
# 25%       63.505620    135.818051
# 50%       66.318070    161.212928
# 75%       69.174262    187.169525
# max       78.998742    269.989699

print('---------- Modifying a DataFrame ----------')
data = [
    {'Name': 'Zhang San', 'Country': 'China', 'City': 'Hangzhou'},
    {'Name': 'Li Si', 'Country': 'China', 'City': 'Shanghai'},
    {'Name': 'Jack', 'Country': 'American', 'City': 'Washington'}
]
df = pd.DataFrame(data)
print(df)
# output
#         Name   Country        City
# 0  Zhang San     China    Hangzhou
# 1      Li Si     China    Shanghai
# 2       Jack  American  Washington

print('---------- Adding a New Column ----------')
weights = [65, 75, 80]
heights = [170, 175, 180]
df['Weight'] = weights
df['Height'] = heights
print(df)
# output
#         Name   Country        City  Weight  Height
# 0  Zhang San     China    Hangzhou      65     170
# 1      Li Si     China    Shanghai      75     175
# 2       Jack  American  Washington      80     180

print('---------- Modifying column values ----------')
df['Height'] = df['Height'] * 0.01
print(df)


# output
#         Name   Country        City  Weight  Height
# 0  Zhang San     China    Hangzhou      65    1.70
# 1      Li Si     China    Shanghai      75    1.75
# 2       Jack  American  Washington      80    1.80

def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi


bmi = calculate_bmi()
df['BMI'] = bmi
print(df)
# output
#         Name   Country        City  Weight  Height        BMI
# 0  Zhang San     China    Hangzhou      65    1.70  22.491349
# 1      Li Si     China    Shanghai      75    1.75  24.489796
# 2       Jack  American  Washington      80    1.80  24.691358

print('---------- Formating DataFrame columns ----------')
df['BMI'] = round(df['BMI'], 1)
print(df)
# output
#         Name   Country        City  Weight  Height   BMI
# 0  Zhang San     China    Hangzhou      65    1.70  22.5
# 1      Li Si     China    Shanghai      75    1.75  24.5
# 2       Jack  American  Washington      80    1.80  24.7

print('--------------------')
birth_year = ['1990', '1995', '1999']
current_year = pd.Series(2021, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
# output
#         Name   Country        City  ...   BMI  Birth Year  Current Year
# 0  Zhang San     China    Hangzhou  ...  22.5        1990          2021
# 1      Li Si     China    Shanghai  ...  24.5        1995          2021
# 2       Jack  American  Washington  ...  24.7        1999          2021
#
# [3 rows x 8 columns]

print('---------- Checking data types of Column values ----------')
print(df.Weight.dtype)  # int64
print(df['Birth Year'].dtype)  # object
df['Birth Year'] = df['Birth Year'].astype('int')
df['Current Year'] = df['Current Year'].astype('int')
print(df['Birth Year'].dtype)  # int32

ages = df['Current Year'] - df['Birth Year']
df['Ages'] = ages
print(df)
# output
#         Name   Country        City  ...  Birth Year  Current Year  Ages
# 0  Zhang San     China    Hangzhou  ...        1990          2021    31
# 1      Li Si     China    Shanghai  ...        1995          2021    26
# 2       Jack  American  Washington  ...        1999          2021    22
#
# [3 rows x 9 columns]

# 过滤数据
print('---------- Age > 30 ----------')
print(df[df['Ages'] > 30])

# output
#         Name Country      City  Weight  ...   BMI  Birth Year  Current Year  Ages
# 0  Zhang San   China  Hangzhou      65  ...  22.5        1990          2021    31
#
# [1 rows x 9 columns]

print('---------- Age <= 30 ----------')
print(df[df['Ages'] <= 30])
# output
#     Name   Country        City  Weight  ...   BMI  Birth Year  Current Year  Ages
# 1  Li Si     China    Shanghai      75  ...  24.5        1995          2021    26
# 2   Jack  American  Washington      80  ...  24.7        1999          2021    22
#
# [2 rows x 9 columns]
