#ROCK PAPER SCISORS

import random

choose = ['nożyce', 'papier', 'kamień']

def gra(x, y):

    if x == "papier" and y== "papier" :
        print(f'Remis! ')

    if x == "papier" and y== "kamień" :
        print(f'Wygrywa: {x}! ')

    if x == "papier" and y== "nożyce" :
        print(f'Wygrywa: {y}!')

    if x == "kamień" and y== "papier":
        print(f'Wygrywa: {y}!')

    if x == "kamień" and y== "kamień" :
        print(f'Remis!')

    if x == "kamień" and y== "nożyce" :
        print(f'Wygrywa: {x}!')

    if x == "nożyce" and y== "papier":
        print(f'Wygrywa: {x}!')

    if x == "nożyce" and y== "kamień" :
        print(f'Wygrywa {y}!')

    if x == "nożyce" and y== "nożyce":
        print(f'Remis!')


#choice of player #1

player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))
player2=random.choice(choose)
print(player2)

#choice of player #2

#player2=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

gra(player1, player2)


