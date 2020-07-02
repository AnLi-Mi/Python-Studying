#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number,
#then tell them whether they guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken,
#and when the game ends, print this out.

# ------------------Solution----------------


import random

#preparing a pull computer choose his number from
pull = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#generating random number between 1 and 9

num = random.choice(pull)
exit="no"

while exit=="no":

    # user is guessing a number

    guess= int(input(f'Zgadnij cyfere miedzy 1 a 9: '))


    # ponownie zapytanie az uzytkownik poprawnie wpisze swoj wybor
    while guess not in range(1,10):
        guess = int(input(f'Niepoprawny wybór, wybierz cyfre miedzy 1 a 9: '))

    # zasady gry
    if guess==num:
        print ('Zgadłeś!')
    elif guess<num:
        print ('Za niska...')
    else:
        print ('Za wysoka...')
               
    print(f'Wyslosowana liczba to: {num}')

    exit= str(input(f'Wpisz "exit" jeśli chcesz zakończyć grę: '))

    if exit == "exit":
        
        print(f'Dziękuję za grę!')
        break
    else:
        continue
