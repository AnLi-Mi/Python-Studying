# This program generates a date of a day in given number of days.
# It's usefull for users who need to arrange i.e. doctors check-ups every specific numbers of days.

# Downloading necesary modules

import datetime
from datetime import date
from datetime import timedelta



# Asking user to indicate the starting date:
#print('Enter the date you want to start counting from')
#start_yr = int(input('year: '))
#start_mo = int(input('month: '))
#start_day = int(input('day: '))


# Asking user to indicate th number of days they want to calculate:

#num = int(input('Enter the number of days you want to count:  '))


# converting the input into datetime attributes
#days = timedelta(days = num)

def create_date(start_yr, start_mo, start_day):
    
    try:
        start_date= date(start_yr, start_mo, start_day)
        print (start_date)
        future_date = (start_date + days) 
        print (f'In {num} days from {start_date} will be {future_date}')

    except ValueError:
        print ("Incorrect entered date so we will use today's date as a default")
        start_date=date.today()
        future_date = (start_date + days) 
        print (f'In {num} days from {start_date} will be {future_date}')
  

print('Enter the date you want to start counting from')
start_yr = int(input('year: '))
start_mo = int(input('month: '))
start_day = int(input('day: '))
num = int(input('Enter the number of days you want to count:  '))
days = timedelta(days = num)


#generating the future date

create_date(start_yr, start_mo, start_day)

#future_date = (start_date + days) 




