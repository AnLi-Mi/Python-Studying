print('Project - Trading game simulation')

import random

bag=['green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red']
wallet = 1000
los = random.choice(bag)
print(los)
if los=='green':
    print('You won!')
else:
    print('You lost!')
