#Let’s say I give you a list saved in a variable:
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list a
#and makes a new list that has only the even elements of this list in it.

# -------------------------SOLUTION----------------------

#creating a function that generats new list out off even elements of given list

def even_list(x):
    #preparing an empty list to populate it with even elements form list x
    b = []
    #going through all elements of the list x and checking if they are dividable by 2
    for i in x:
        if i%2==0:
            # populating the list b with even elelemnts of x
            b.append(i)
    print(b)


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list(a)
