#Write a function that takes an ordered list of numbers
#(a list where the elements are in order from smallest to largest)
#and another number.
#The function decides whether or not the given number is inside the list
#and returns (then prints) an appropriate boolean.

# ------------------------------solution -------------------


def element_search(x,y):

    #convering an entered string of digits into a list of single digits
    x=list(x)
    #ordering the list
    x.sort()
    print('The given list is: ', x)
    if y in x:
        print(True)
    else:
        print(False)


a=input('Please enter a list of numbers: ')
b=input('Please enter a number you are searching: ')

element_search(a,b)
    
