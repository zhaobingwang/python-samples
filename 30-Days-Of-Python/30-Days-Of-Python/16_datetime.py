from datetime import datetime

print('---------- Getting datetime Information ----------')
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.timestamp())  # Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

print('---------- Formating Date Output Using strftime ----------')
new_year = datetime(2021, 1, 1)
print(new_year)
year = new_year.year
month = new_year.month
day = new_year.day
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(year, month, day, hour, minute, second)
print(f'{year}/{month}/{day}, {hour}:{minute}:{second}')

# Time formating
print('\t---------- Time formating ----------')
now = datetime.now()
t = now.strftime('%Y-%m-%d %H:%M:%S')
print(t)

print('---------- String to Time Using strptime ----------')

date_string = "2021-01-01"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print("date_object =", date_object)

print('---------- Using date from datetime ----------')
from datetime import date

d = date(2021, 2, 7)
print(d)  # 2021-02-07
print(d.day)  # 7
print(d.today())  # date object of today's date

print('---------- Time Objects to Represent Time ----------')
from datetime import time

print(time())  # 00:00:00
print(time(12, 00, 00))  # 12:00:00
print(time(hour=12, second=0, minute=30))  # 12:30:00

print('---------- Difference Between Two Points in Time Using ----------')

today = date(year=2021, month=2, day=7)
new_year = date(2022, 1, 1)
time_remaining_of_new_year = new_year - today
print('Remaining time of New Year:', time_remaining_of_new_year)

today = datetime(year=2021, month=2, day=7, hour=0, minute=0, second=0)
new_year = datetime(year=2022, month=1, day=1, hour=0, minute=0, second=0)
time_remaining_of_new_year = new_year - today
print('Remaining time of New Year:', time_remaining_of_new_year)

print('---------- Difference Between Two Points in Time Using timedelta ----------')
# 更多信息参见：https://docs.python.org/zh-cn/3/library/datetime.html#timedelta-objects
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
