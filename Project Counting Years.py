# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them
# the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number
#and printing out that many copies of the previous message.
#Hint: order of operations exists in Python
#Print out that many copies of the previous message on separate lines. 
#Hint: the string "\n is the same as pressing the ENTER button

#------------------------------solution----------------------------

# importing datetime module to automatate the proces

from datetime import date

current_yr=date.today().year

# defining name and age as an intput

name = str(input(f'Please enter your name: '))
age = int(input(f'Please enter your age: '))
num = int(input(f'Choose random number between 1 and 10:  '))


if num not in range (1,10) :
    num = (int(input(f'Wrong number, please choose one between 1 and 10: ')))
    
if num in range (1,10):
    for i in range (num):
        print (f'Hi {name}! You will turn 100 in {100-age} years. It will be year {current_yr + 100 - age}.' )




   
