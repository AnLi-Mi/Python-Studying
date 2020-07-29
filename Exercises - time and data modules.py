# Exercise:  Write a Python program to determine whether a given year is a leap year.

import datetime
from datetime import date
from datetime import timedelta

# asking user to input the year they want to check:

year = int(input("Please neter a year to check if it'a leap year: "))

# 60th day of a year can be 29of feb or 1st of march,
# therefore I create a timedelta calculating 59 days from the begining of a given year

future = timedelta(days = 59)
start_date = date(year, 1,1)

# generating the date of a 60th day of a given year
check_date = start_date + future

# checking if a month of a generated date was february or march
if check_date.month == 2:
    print (f'{year} is a leap year')
else:
    print (f'{year} is NOT a leap year')

