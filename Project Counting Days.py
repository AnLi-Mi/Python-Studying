# This program generates a date of a day in given number of days.
# It's usefull for users who need to arrange i.e. doctors check-ups every specific numbers of days.

# Downloading necesary modules

import datetime
from datetime import date
from datetime import timedelta



# Asking user to indicate the starting date:
print('Enter the date you want to start counting from')
start_yr = int(input('year: '))
start_mo = int(input('month: '))
start_day = int(input('day: '))
# Asking user to indicate th number of days they want to calculate:

num = int(input('Enter the number of days you want to count:  '))


# converting the input into datetime attributes

start_date= date(start_yr, start_mo, start_day)

days = timedelta(days = num)

#generating the future date

future_date = (start_date + days) 

print (f'In {num} days from {start_date} will be {future_date}')



