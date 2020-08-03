import anna_module

print(dir(anna_module))

name = input(f"What's your name? ")

anna_module.greeting(name)

#importing specific pull for the  game
pull = anna_module.srp_pull

#randomly selecting one item from the imported list 
guess = anna_module.random_selection(pull)

#requesting input from the user
choice = input(f'Choose one item from: {pull}')
#impementing imported function to request typing correct value
anna_module.correct_str_input_request(choice,pull)

#showing the result
anna_module.rps_comparing(guess, choice)


