#Create a program that will play the “cows and bulls” game with the user.
#The game works like this:
#Randomly generate a 4-digit number.
#Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place,
#they have a “cow”.
#For every digit the user guessed correctly in the wrong place is a “bull.”
#Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout the game
#and tell the user at the end.


#-----------------------------SOLUTION------------------------------

import random as r

#generating random 4-digit number
number = r.choice(range(1000,10000))
print(number)

#asking user to guess a number

guess=int(input('Guess a 4-digit number: '))

while guess not in range(1000,10000):
    guess=int(input("It's not a 4-digit number....Guess a number between 1000 and 9999: "))




                  
