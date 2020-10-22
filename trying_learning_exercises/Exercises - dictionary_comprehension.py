users = [(0,"Bob", "password1"),
         (1,"Alice", "cat's_name"),
         (2,"Steven", "1234"),
         (3,"Chris", "xxhwh6e3")]

# creating the dictionary option1

users_dictionary = {}

i=1
while i<=len(users):
    for user in users:
        users_dictionary[user[1]] = user
        i+=1


print(users_dictionary)


# creating the dictionary option2

users_dictionary2 = {user[1]:user for user in users}


print(users_dictionary2)


# adding the user from the user's input

username_input = input('Enter your name: ')
password_input = input('Choose your password: ')

users_dictionary[username_input] = len(users_dictionary2), username_input, password_input

print(users_dictionary)

# checking the correctness of an inputed values

username_input2 = input('Enter your name: ')



if username_input2 in users_dictionary2.keys():
    _, username, password = users_dictionary2[username_input2]
    password_input2 = input('Enter your password: ')
    if password_input2 == password:
        print ('Access allowed!')
    else:
        print ('Wrong password')
else:
   print('you ar not registered user!')
          
    
    

