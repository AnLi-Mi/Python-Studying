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


# adding the user from the input

user_name = input('Enter your name: ')
user_password = input('Chooser your name: ')

users_dictionary2[user_name] = len(users_dictionary2), user_name, user_password

print(users_dictionary2)

