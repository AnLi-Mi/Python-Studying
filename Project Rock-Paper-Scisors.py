#ROCK PAPER SCISORS

import random

score = 0
game='tak'
games=0

while game.lower()=='tak':

    #choice of player #1
    player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

    #requesting the input until it's correct
    while player1.lower() not in ['nożyce', 'papier', 'kamień']:
        player1=str(input(f'Nieprawidłowy wybór. Wybirz "papier", "nożyce" czy "kamień": '))
        
    #losowy wybór komputera:
    choose = ['nożyce', 'papier', 'kamień']
    player2=random.choice(choose)
    print(f'Komputer wybrał: {player2}')

    #zasady gry
    if player1.lower() == player2:
        print(f'Remis! ')
    elif (player1.lower() == "papier" and player2== "kamień") or (player1.lower() == "kamień" and player2== "nożyce") or (player1.lower() == "nożyce" and player2== "papier")  :
        print(f'Wygrywa: {player1}! ')
        score=score+1
    else:
        print(f'Wygrywa: {player2}!')
    games+=1
            
    game=str(input(f'Wpisz "tak" jeśłi chcesz zagrać ponownie: '))
        
    

print(f'Dziękuejmy za grę! Zdobyłeś {score}/{games} puntów')





