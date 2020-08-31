#Ask the user for a string and print out whether this string is a palindrome or
#not. (A palindrome is a string that reads the same forwards and backwards.)


#--------------------SOLUTION-----------------------

# function detecting palindromes

def palindrome(x):
    if x == x[::-1]:
        print(f'"{x}" is a palindrome')
    else:
        print(f'"{x}" is not a palindrome')

# requesting an input from a user
word = str(input(f"Please enter a string to check if it's a palindrome: "))

# running the function for a string given by the user

palindrome(word)
    
    
