print ('------------------- Exercise 1 ----------------------')

# Exercise 1:  Write a Python program to determine whether a given year is a leap year.

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

print ('------------------- Exercise 2 ----------------------')
# Exercise 2: Write a Python program to print yesterday, today, tomorrow.

diff = timedelta(days =1)

today = date.today()
tomorrow = today + diff
yesterday  = today - diff

print (yesterday, today, tomorrow)

print ('------------------- Exercise 3 ----------------------')

# Exercise 3: Write program to get current time in seconds in Python

# datetime object containing current date and time
now = datetime.now()

# extracting elements of the current date
hour = int(now.hour)
minute= int(now.minute)
second = int(now.second)

print(f"Current time is {hour} : {minute} : {second}")

#creating timedelta to calculate number of seconds

time = timedelta(hours = hour, minutes = minute ,seconds= second)

	
print(f" it's {time.total_seconds()} seconds of the day")

print ('------------------- Exercise 4 ----------------------')

# Exercise 4: Write a Python program to get a list of dates between two dates. 

#importing necessary modules
from datetime import date
from datetime import datetime
from datetime import timedelta

#asking user for the input of two dates

date1 = input('Enter first date (dd/mm/yyyy): ')
date2 = input ('Enter second date (dd/mm/yyyy): ')

#convering the inputed strings into a date format

date1 = datetime.strptime(date1, "%d/%m/%Y")
date2 = datetime.strptime(date2, "%d/%m/%Y")

#preparing timedelta object of one day to raise each day with one day(something like a step)
t = timedelta(days =1)
#starting the loop from fist given date
i = date1

#a loop printing each day and adding one more day until it reaches a second given date
while i <= date2:
    print (i.date())
    i =  i + t



print ('------------------- Exercise 5 ----------------------')

# Exercise 5: 3. Write a Python program to convert a string to datetime.
#Sample String : Jan 1 2014 2:43PM
#Expected Output : 2014-07-01 14:43:00

import datetime
from datetime import datetime

str_date = "Jan 1 2014 2:43PM"
dt_date = datetime.strptime(str_date, "%b %d %Y %I:%M%p")
print (f'String format: {str_date}')
print (f'Datetime format: {dt_date}')

