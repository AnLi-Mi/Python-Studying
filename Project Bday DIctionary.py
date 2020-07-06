#For this exercise, we will keep track of when our friend’s birthdays are,
#and be able to find that information based on their name.
#Create a dictionary (in your file) of names and birthdays.
#When you run your program it should ask the user to enter a name,
#and return the birthday of that person back to them.

# ------------------------------SOLUTION------------------

# creating a dictionary with data
bdays = {
    "Tut":'02/19',
    "Polajn":'01/19',
    "Gug":'06/26',
    "Mart":'12/03',
    "Tomasz":'10/11'}

#input the name

name = input("Insert a name of your friend: ")

#returning the birthday's data

print (f"{name}'s birthady is on {bdays[name]}.")



    
