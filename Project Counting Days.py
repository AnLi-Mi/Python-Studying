# This program generates a date of a day in given number of days.
# It's usefull for users who need to arrange i.e. doctors check-ups every specific numbers of days.

# Downloading necessary modules

import datetime
from datetime import date
from datetime import timedelta


# creating a function generating a starting date form given veriables
#and than adding given number of days
def create_date(date_str, num):
    from datetime import datetime
    try:
        #convering a given string into date format
        start_date = datetime.strptime(date_str, "%d/%m/%Y")
        #converting the input into timedalta attribute
        days = timedelta(days = num)
        #generating the future date
        future_date = (start_date + days) 
        print (f'In {num} days from {start_date} will be {future_date}')

    except ValueError:
        print ("Incorrect entered date so we will use today's date as a default")
        #creating default date if ValueError
        start_date=date.today()
        #converting the input into timedalta attribute
        days = timedelta(days = num)
        #generating the future date
        future_date = (start_date + days) 
        print (f'In {num} days from {start_date} will be {future_date}')
        
  
# asking user to indicate th number of days they want to calculate:
date_str = input('Enter the date you want to start counting from (dd/mm/yyy): ' )

# asking user to indicate th number of days they want to calculate:
num = int(input('Enter the number of days you want to count:  '))

#calling the function with given virables
create_date(date_str, num)

 




