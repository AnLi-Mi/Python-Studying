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

exit="no"
score=0
games=0

print(f'Witaj! Masz 3 podejście aby zgadnąć wylosowaną liczbę!')

while exit!="exit":

    
    #generating random number between 1 and 9
    num = random.choice(pull)
    
    
    # loop allowing 3 attempts
    i=1
    while i<4:    

        # user is guessing a number

        guess= int(input(f'Podejście {i}: Zgadnij cyfrę między 1 a 9: '))

        # ponownie zapytanie az uzytkownik poprawnie wpisze swoj wybor
        while guess not in range(1,10):
            guess = int(input(f'Niepoprawny wybór, wybierz cyfrę między 1 a 9: '))

        # zasady gry:
        if guess==num:
            print (f'Zgadłeś za {i} razem!')
            score+=1
            break
        elif guess<num:
            print ('Za niska...')
        else:
            print ('Za wysoka...')
        i+=1
               
    print(f'Wyslosowana liczba to: {num}')

    games+=1

    exit= str(input(f'Wpisz "exit" jeśli nie chcesz dalej: '))

    if exit == "exit":
        
        print(f'Dziękuję za grę! Twój wynik to {score}/{games}')
        break
    
