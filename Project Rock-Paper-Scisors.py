#ROCK PAPER SCISORS

#choice of player #1

player1=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

#choice of player #2

player2=str(input(f'Wybirz "papier", "nożyce" czy "kamień": '))

if player1 == "papier" and player2== "papier" :
    print(f'Remis! ')

if player1 == "papier" and player2== "kamień" :
    print(f'Wygrywa: {player1}! ')

if player1 == "papier" and player2== "nożyce" :
    print(f'Wygrywa: {player2}!')

if player1 == "kamień" and player2== "papier":
    print(f'Wygrywa: {player2}!')

if player1 == "kamień" and player2== "kamień" :
    print(f'Remis!')

if player1 == "kamień" and player2== "nożyce" :
    print(f'Wygrywa: {player1}!')

if player1 == "nożyce" and player2== "papier":
    print(f'Wygrywa: {player1}!')

if player1 == "nożyce" and player2== "kamień" :
    print(f'Wygrywa {player2}!')

if player1 == "nożyce" and player2== "nożyce":
    print(f'Remis!')
