print('Project - Trading game simulation')

import random

bag=['green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red']
wallet = 1000
games = int(input('how many times do you want to play?: '))

for game in range (1,games+1):                 
    bet = int(input('How much do you bet?: '))
    los = random.choice(bag)
    print(los)
    if los=='green':
        print('You won!')
        wallet = wallet + bet
        print (f'You have {wallet}$') 
    else:
        print('You lost!')
        wallet = wallet - bet
        print (f'You have {wallet}$')


