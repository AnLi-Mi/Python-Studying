# Exercise:  Write a Python program to determine whether a given year is a leap year.

import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def leap_year(year):
    # 60th day of a year can be 29of feb or 1st of march,
# therefore I create a timedelta calculating 59 days from the begining of a given year

    future = timedelta(days = 59)
    start_date = date(year, 1,1)

# generating the date of a 60th day of a given year
    check_date = start_date + future

# checking if a month of a generated date was february or march
    if check_date.month == 2:
       return True
    else:
        return False

# asking user to input the year they want to check:

yr = int(input("Please enter a year to check if it's a leap year: "))

print(leap_year(yr))


# Exercise 2: Write a Python program to print yesterday, today, tomorrow.

diff = timedelta(days =1)

today = date.today()
tomorrow = today + diff
yesterday  = today - diff

print (yesterday, today, tomorrow)

# Exercise 3: Write program to get current time in milliseconds in Python

# datetime object containing current date and time
now = datetime.now(hour, minute, second)
print (now)
time = now.strftime("%H:%M:%S")
#time2 = timedelta(hours = %H, minutes = %M ,seconds= %S)
print(f"Current time is {time}")	
print(time.total_seconds())
