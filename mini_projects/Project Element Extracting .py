#Write a program that takes a list of numbers
#(for example, a = [5, 10, 15, 20, 25]) and
#makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.

#------------------------SOLUTION---------------------

def lista(x):
    b = [x[0], x[-1]]
    print(f'Pierwszy i ostatni element to: {b}')

a= [5, 10, 15, 20, 25]

lista(a)
