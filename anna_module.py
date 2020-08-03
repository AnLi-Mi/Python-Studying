def greeting(name):

    print (f'Hello {name.capitalize()}!')


def correct_input_request(guess,pull):
        
        # ponownie zapytanie az uzytkownik poprawnie wpisze swoj wybor
        while guess not in pull:
            guess = input(f'Wrong input, please choose again from {pull}: ')



numbers_pull = range(1,11)

animal_pull = ["cat", "dog", "lion", "parrot", "snake", "rabbit", "graffe", "mouse", "pig", "donkey"]

srp_pull = ["scisors", "rock", "paper"]
