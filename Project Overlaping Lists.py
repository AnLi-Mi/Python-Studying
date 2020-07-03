#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only
#the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.
#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python

#---------------------------SOLUTION---------------------

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#preparing an empty list to generate it with common numbers
c=[]

#solution with 'in'
for i in a:
    if i in b:
            c.append(i)

#turning into a set to get rid of duplicates
c=set(c)
#turnig back to list again
print (f'Wspólnymi elementami obu list są: {list(c)}')



