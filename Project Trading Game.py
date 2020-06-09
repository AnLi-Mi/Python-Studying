print('Project - Trading game simulation')

import random

bag=['green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red']
wallet = 1000
games = int(input('how many times do you want to play?: '))


for game in range (1, games+1):                 
    bet = int(input('How much do you bet?: '))
    los = random.choice(bag)
    print(los)
    if los=='green':
        wallet = wallet + bet
        print (f'Great! You have {wallet}$') 
    else:
        wallet = wallet - bet
        print (f'Oh, no... You have {wallet}$')
    if wallet <500:
        print ('You lost... You have less than 500$, you can not play')
        break
        
   # playing = str(input('Do you still want to play?; '))


