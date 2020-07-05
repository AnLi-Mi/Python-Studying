#Write a program (function!) that takes a list and returns a new list
#that contains all the elements of the first list minus all the duplicates.
#Extras:
#Write two different functions to do this -
#one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets,
#and write the solution for that in a different function.

#--------------SOLUTION 1 with loop -------------


def remove_dup1(a):
    #preparing and empty list to populate with elements from list a
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print (b)


test = [1, 1, 2, 2, 3, 6 , 8, 3, 2, 1]

remove_dup1(test)

#--------------SOLUTION 2 with sets -------------
        
def remove_dup2(x):
    x = set(x)
    x = list(x)
    print (x)

test = [1, 1, 2, 2, 3, 6 , 8, 3, 2, 1]

remove_dup2(test)
    
        

    
