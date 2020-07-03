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

lower_case = list(s.ascii_lowercase)
print(lower_case)
upper_case = list(s.ascii_uppercase)
print(upper_case)
numbers = list(s.digits)
print(numbers)
symbols = list(s.punctuation)
print(symbols)

characters = [lower_case, upper_case, numbers, symbols]



import random as r

def pword():
    # creating empty list to populat it with chosen elements
    pw=[]
    pw.append(r.choice(lower_case))
    pw.append(r.choice(upper_case))
    pw.append(r.choice(numbers))
    pw.append(r.choice(symbols))
    r.shuffle(pw)
    pw="".join(pw)
    print(pw)

pword()
