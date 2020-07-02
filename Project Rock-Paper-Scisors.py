#ROCK PAPER SCISORS

import random

choose = ['nożyce', 'papier', 'kamień']

def gra(x, y):

    if x == y:
        print(f'Remis! ')
    elif (x == "papier" and y== "kamień") or (x == "kamień" and y== "nożyce") or (x == "nożyce" and y== "papier")  :
        print(f'Wygrywa: {x}! ')
    else:
        print(f'Wygrywa: {y}!')

    


#choice of player #1

player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

#requesting the input until it's correct

while player1 not in ['nożyce', 'papier', 'kamień']:
    player1=str(input(f'Nieprawidłowy wybór. Wybirz "papier", "nożyce" czy "kamień": '))
    

#losowy wybór komputera:
player2=random.choice(choose)
print(f'Komputer wybrał: {player2}')

#choice of player #2

#player2=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

gra(player1, player2)


