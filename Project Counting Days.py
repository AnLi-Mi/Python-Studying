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
days = timedelta(days = num)

    # Default today's date
if start_yr == 0 or start_mo not in (1 ,12) or start_day not in (1,31):
    start_date=date.today()
else:
    #start_yr = int(start_yr)
    #start_mo = int(start_mo)
    #start_day = int(start_day)
    start_date= date(start_yr, start_mo, start_day)



#generating the future date

future_date = (start_date + days) 

print (f'In {num} days from {start_date} will be {future_date}')



