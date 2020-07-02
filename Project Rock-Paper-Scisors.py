#ROCK PAPER SCISORS

import random

choose = ['nożyce', 'papier', 'kamień']

def gra(x, y):
    score = 0
    if x.lower() == y:
        print(f'Remis! ')
    elif (x.lower() == "papier" and y== "kamień") or (x.lower() == "kamień" and y== "nożyce") or (x.lower() == "nożyce" and y== "papier")  :
        print(f'Wygrywa: {x}! ')
        score=score+1
    
    else:
        print(f'Wygrywa: {y}!')
        
    again=str(input(f'Wpisz "Tak" jeśłi chcesz zagrać ponownie: '))
    
    if again.lower() == "tak":
        #wybór gracz
        player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

        #requesting the input until it's correct
        while player1 not in ['nożyce', 'papier', 'kamień']:
            player1=str(input(f'Nieprawidłowy wybór. Wybirz "papier", "nożyce" czy "kamień": '))
        

        #losowy wybór komputera:
        player2=random.choice(choose)
        print(f'Komputer wybrał: {player2}')

        #ponowna gra
        gra(player1, player2)
        
    else:
        print(f'Dziękuejmy za grę! Zdobyłeś {score} puntów')
    

#choice of player #1

player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

#requesting the input until it's correct

while player1 not in ['nożyce', 'papier', 'kamień']:
    player1=str(input(f'Nieprawidłowy wybór. Wybirz "papier", "nożyce" czy "kamień": '))
    

#losowy wybór komputera:
player2=random.choice(choose)
print(f'Komputer wybrał: {player2}')

#choice of player #2

gra(player1,player2)






