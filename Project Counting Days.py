# This program generates a date of a day in given number of days.
# It's usefull for users who need to arrange i.e. doctors check-ups every specific numbers of days.

# Downloading the date module

import time
import numpy as np

# Creating a list of a days in a year

jan = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
feb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
leap_feb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
mar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
apr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
may = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
jun = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
jul = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
aug = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
sep = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
oct = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
nov = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
dec = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

months = {1:jan, 2:feb, 3:mar, 4:apr, 5:may, 6:jun, 7:jul, 8:aug, 9:sep, 10:oct, 11:nov, 12:dec}


year = jan + feb + mar + apr + may + jun + jul + sep + oct + nov + dec
year1 = np.array([jan, feb, mar, apr, may, jun, jul, sep, oct, nov, dec])
leap_year = jan + leap_feb + mar + apr + may + jun + jul + sep + oct + nov + dec

print(year1)

# Asking user to indicate the number of counted days

num = int(input('Enter the number of days you want to count: '))

# Asking user for a starting day

start_month = int(input('Enter the month of the day you want to count from: '))
start_date = int(input('Enter the day you want to count from: '))
print (year1[start_month, start_date])

# Extracting the day of a given index

day = year [start_date + num-1]

#print (day)


# Extracting a month 

# Extanding the use of the code for upcoming years

# Including leap-years
