import anna_module

name = input(f"What's your name? ")

anna_module.greeting(name)

#importing pull for the rock-paper-scisors game
pull = anna_module.srp_pull

#randomly selecting one item from the imported list 
guess = anna_module.random_selection(pull)
print(guess)

choice = input(f'Choose one item from: {pull}')
anna_module.correct_input_request(choice,pull)


anna_module.comparing(guess, choice)


