import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# Output:
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

dates = pd.date_range('20210506', periods=6)
print(dates)
# Output:
# DatetimeIndex(['2021-05-06', '2021-05-07', '2021-05-08', '2021-05-09',
#                '2021-05-10', '2021-05-11'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
# Output:
#                    A         B         C         D
# 2021-05-06  1.017064  1.203402  0.321319 -1.842937
# 2021-05-07  0.862317 -0.118506  0.965226  1.135190
# 2021-05-08  0.095270 -0.274542  0.065710  0.848447
# 2021-05-09  0.505555  0.910965 -0.640123  0.139648
# 2021-05-10 -1.610411  2.211535 -0.753992  0.745157
# 2021-05-11 -1.252522  0.560822 -0.741799  0.293456


df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20210506'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'
                    })
print(df2)
# Output
#      A          B    C  D      E    F
# 0  1.0 2021-05-06  1.0  3   test  foo
# 1  1.0 2021-05-06  1.0  3  train  foo
# 2  1.0 2021-05-06  1.0  3   test  foo
# 3  1.0 2021-05-06  1.0  3  train  foo

print(df2.dtypes)
# Output
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object

print('# 查看数据')

print('头部数据')
print(df.head)
# <bound method NDFrame.head of                    A         B         C         D
# 2021-05-06 -0.306809  0.422631 -2.093736  0.740021
# 2021-05-07  1.294873  0.576172  0.207939  1.516931
# 2021-05-08 -1.705928  1.726531  0.404730 -0.904943
# 2021-05-09  1.872359 -0.325699  0.355805 -2.472407
# 2021-05-10  2.260158 -1.023984 -0.203169 -1.473089
# 2021-05-11  0.260818 -1.462511  0.449855 -0.308070>

print('最后三条')
print(df.tail(3))
#                    A         B         C         D
# 2021-05-09  1.872359 -0.325699  0.355805 -2.472407
# 2021-05-10  2.260158 -1.023984 -0.203169 -1.473089
# 2021-05-11  0.260818 -1.462511  0.449855 -0.308070

print('索引')
print(df.index)
# DatetimeIndex(['2021-05-06', '2021-05-07', '2021-05-08', '2021-05-09',
#                '2021-05-10', '2021-05-11'],
#               dtype='datetime64[ns]', freq='D')

print('列名')
print(df.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')
