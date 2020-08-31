def greeting(name):
    print (f'Hello {name.capitalize()}, welcome in the game!')


def correct_int_input_request(guess,pull):
        # ponownie zapytanie az uzytkownik poprawnie wpisze swoj wybor
        while guess not in pull:
            guess = int(input(f'Wrong input, please choose again from {pull}: '))

def correct_str_input_request(guess,pull):
        # ponownie zapytanie az uzytkownik poprawnie wpisze swoj wybor
        while guess not in pull:
            guess = input(f'Wrong input, please choose again from {pull}: ')            

def random_selection(pull):
    #losowanie pojedynczego elementu z podanej listy
    import random
    selection = random.choice(pull)
    return selection


def guess_comparing(comp, user):
    if user == comp:
        print ('Congrats! You guessed!')
    else:
        print (f'You lost, the selected item was {comp}.') 

def guess_comparing(comp, user):
    if user == comp:
        print ('Congrats! You guessed!')
    else:
        print (f'You lost, the selected item was {comp}.')

def rps_comparing(comp, user):
    if user.lower() == comp:
        r = "Remis!"
        return r 
    elif (user.lower() == "paper" and comp== "rock") or (user.lower() == "rock" and comp== "scisors") or (user.lower() == "scisors" and comp== "paper")  :
        r = "You won!"
        return r
    else:
        r = "You lost..."
        return r
        
#przykłady list
numbers_pull = range(1,11)

animal_pull = ["cat", "dog", "lion", "parrot", "snake", "rabbit", "graffe", "mouse", "pig", "donkey"]

srp_pull = ["scisors", "rock", "paper"]
