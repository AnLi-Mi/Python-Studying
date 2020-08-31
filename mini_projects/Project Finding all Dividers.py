#Create a program that asks the user for a number and
#then prints out a list of all the divisors of that number.

# -----------------------solution---------------------

#asking user to choose a number
num = int(input('Proszę podać dowolną liczbę: '))
#preparing a list to fill it out with chosen number's diveders
dividers=[]

# loop checjing all numbers below the chosen number if they are its dividers:

for i in range (1, num+1):
    if num%i==0:
        dividers.append(i)

# printing a solution

print (f'Dzielnikami {num} są: {dividers}')
