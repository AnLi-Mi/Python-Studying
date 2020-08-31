# Implement a function that takes as input three variables,
#and returns the largest of the three.
#Do this without using the Python max() function!
#The goal of this exercise is to think about some
#internals that Python normally takes care of for us.
#All you need is some variables and if statements!

#--------------------SOLUTION ---------------

#requestig an inpit of 3 numbers

numbers = input('Please enter 3 numbers: ')

# turning a string input into a list of numbers

numbers = list(numbers.split(' '))

# returning the highest number

print (f'The highest number is: {max(numbers)}')
