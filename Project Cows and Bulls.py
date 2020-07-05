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
number = r.choices(range(1,10), k=4)
print(number)

#asking user to guess a number

guess=str(input('Guess a 4-digit number: '))
#turning the guessed number to a list of intigers
guess =[int(guess[0]),int(guess[1]),int(guess[2]), int(guess[3])]

#while guess not in range(1000,10000):
 #   guess=(input("It's not a 4-digit number....Guess a number between 1000 and 9999: "))

#preparing a couter of 'cows' and 'bulls'
cows=0
bulls=0

#counting 'cows' - checking if the user guessed any of the digits correctly in the correct place
#for i in guess:
 #  if i == number[i]:
  #     print('wygrales krowe')

#counting 'bulls' - checking if the user guessed any of the digits correctly but not in the correct place
        
for i in guess:
    if i in number:
        bulls+=1

print(f" You won {bulls} bulls and {cows} cows!")


                  
