#Write a function that takes an ordered list of numbers
#(a list where the elements are in order from smallest to largest)
#and another number.
#The function decides whether or not the given number is inside the list
#and returns (then prints) an appropriate boolean.

# ------------------------------solution -------------------


def element_search(x,y):
    x.sort()
    if y in x:
        print(True)
    else:
        print(False)


a=[9,9,4,5,6,9,6,5,3,1,2,3,5]
b=9

element_search(a,b)
    
