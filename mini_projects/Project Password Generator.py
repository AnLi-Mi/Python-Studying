#Write a password generator in Python.
#Be creative with how you generate passwords -
#strong passwords have a mix of:
#lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random,
#generating a new password every time the user asks for a new password.
#Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be.


#-------------------------------solution----------------------

# generating lists of obligatory elements for a strong password
import string as s

# importing lists of password's potential characters, to choose from

lower_case = list(s.ascii_lowercase)
upper_case = list(s.ascii_uppercase)
numbers = list(s.digits)
symbols = list(s.punctuation)



import random as r


# function for a weak passowrd - 8 charakters, which are mix of lowercase and number

def pword_weak():
    # creating a list of types of characters to choose from
    characters_pull = [lower_case, numbers]

    # creating empty list to populat it with chosen elements
    pw=[]
    # setting a default password lenthg for 8 characters)
    pw_l=8

    # sequring at least one character of each obligatory type
    pw.append(r.choice(lower_case))
    pw.append(r.choice(numbers))

    # randomly selecting types of rest of characters
    for i in range (3, pw_l+1):
        # randomly choosing a type of character
        char=r.choice(characters_pull)
        # randomly choosing a character from the selected type
        pw.append(r.choice(char))

    # shuffling all selected elements 
    r.shuffle(pw)

    # turning a list of elelemts into a string
    pw="".join(pw)
    print(f'Twoje hasło to: {pw}')


# function for a midium passowrd - 10 charakters, which are mix of upper and lowercase and number

def pword_medium():
    # creating a list of types of characters to choose from
    characters_pull = [lower_case, upper_case, numbers]

    # creating empty list to populat it with chosen elements
    pw=[]
    # setting a default password lenthg for 12 characters)
    pw_l=12

    # sequring at least one character of each obligatory type
    pw.append(r.choice(lower_case))
    pw.append(r.choice(upper_case))
    pw.append(r.choice(numbers))

    # randomly selecting types of rest of characters
    for i in range (4, pw_l+1):
        # randomly choosing a type of character
        char=r.choice(characters_pull)
        # randomly choosing a character from the selected type
        pw.append(r.choice(char))

    # shuffling all selected elements 
    r.shuffle(pw)

    # turning a list of elelemts into a string
    pw="".join(pw)
    print(f'Twoje hasło to: {pw}')



# function for a strong passowrd - min 12 characters, which are a mix of:lowercase letters, uppercase letters, numbers, and symbols
def pword_strong():

    # creating a list of types of characters to choose from
    characters_pull = [lower_case, upper_case, numbers, symbols]

    # creating empty list to populat it with chosen elements
    pw=[]

    # asking user to choose a length of their password (setting a min lenthg of password 12 characters)
    pw_l=int(input(f"Jaką długość ma mieć hasło (min 12 znaków)?: "))
    # repetedly ask user for a length of the password until it's chosen correctly
    while pw_l <12:
        pw_l=int(input(f"Za niska liczba znaków (min 12 znaków). Ponwnie podaj liczbę znaków: "))
        
    # sequring at least one character of each obligatory type
    pw.append(r.choice(lower_case))
    pw.append(r.choice(upper_case))
    pw.append(r.choice(numbers))
    pw.append(r.choice(symbols))

    # randomly selecting types of rest of characters
    for i in range (5, pw_l+1):
        # randomly choosing a type of character
        char=r.choice(characters_pull)
        # randomly choosing a character from the selected type
        pw.append(r.choice(char))

    # shuffling all selected elements 
    r.shuffle(pw)

    # turning a list of elelemts into a string
    pw="".join(pw)
    print(f'Twoje hasło to: {pw}')


level = str(input(f'Jak mocne ma być hasło "strong", "medium" czy "weak"?: '))

while level not in ["strong", "medium", "weak"]:
    level=str(input(f'Niepoprawny wybór, wpisz "strong", "medium" albo "weak"'))

if level =="weak":
    pword_weak()
elif level =="medium":
    pword_medium()
else:
    pword_strong()

