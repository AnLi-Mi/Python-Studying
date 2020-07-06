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

def twist(x):
    
    #turnig one string into a list of single words
    words = rym.split()
    
    #creating an empty list to populate it with the words in new order
    rym_twist =[]
    
    # swaping places of the words
    # creating two alternatives to avid indexerror for a strings with odd number of words
    if len(words)%2==0:
        
        for i in range (0, len(words),2):
           rym_twist.insert(i, words[i+1])
                  
            
        for i in range (1, len(words),2):
            rym_twist.insert(i, words[i-1])
    else:
        for i in range (0, len(words)-1,2):
           rym_twist.insert(i, words[i+1])

        
        for i in range (1, len(words),2):
            rym_twist.insert(i, words[i-1])

      
        
    #turning the new list into a sting
    rym_twist=" ".join(rym_twist)
    print (rym_twist)


twist(rym)
 
                    
