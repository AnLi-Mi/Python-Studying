import anna_module

anna_module.greeting("Anna")


pull = anna_module.srp_pull
choice = input(f'Choose one item from: {pull}')

anna_module.correct_input_request(choice,pull)



