#Write a password generator in Python.
#Be creative with how you generate passwords -
#strong passwords have a mix of:
#lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random,
#generating a new password every time the user asks for a new password.
#Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be.
#For weak passwords, pick a word or two from a list.

#-------------------------------solution----------------------

# generating lists of obligatory elements for a strong password
import string as s

# importing lists of password's potential characters, to choose from

lower_case = list(s.ascii_lowercase)
upper_case = list(s.ascii_uppercase)
numbers = list(s.digits)
symbols = list(s.punctuation)

# creating a list of types of characters to choose from
characters_pull = [lower_case, upper_case, numbers, symbols]

import random as r

# function for a strong passowrd
def pword():
    
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
        # randomly choosing a character from the selected typ
        pw.append(r.choice(char))
    # shuffling all selected elements 
    r.shuffle(pw)
    # turning a list of elelemts into a string
    pw="".join(pw)
    print(f'Twoje hasło to: {pw}')

pword()

# jutro: wybrac dlugosc hasla, losownie typow elementow z 4 narzuconymi, users input
