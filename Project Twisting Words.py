#Write a program (using functions!) that asks the user for a
# long string containing multiple words.
# Print back to the user the same string,
#except with the words in backwards order.
#For example, say I type the string:
#My name is Michele
#Then I would see the string:
#Michele is name My
#shown back to me.

#-------------------------SOLUTION ------------------------------

# asking to user to input the string

rym = str(input("Please type in a short paragraph: "))

#def twist(x):
#turnig one string into a list of single words
words = rym.split()
print (words)
 
                    
