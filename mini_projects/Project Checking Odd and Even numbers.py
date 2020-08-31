#Ask the user for a number.
#Depending on whether the number is even or odd,
#print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#1-If the number is a multiple of 4, print out a different message.
#2- Ask the user for two numbers: one number to check (call it num)
#and one number to divide by (check).
#If check divides evenly into num, tell that to the user.
#If not, print a different appropriate message.

#---------------Solution---------------

#requesing the user for the numbers

num = int(input('Proszę podać dowolną liczbę: '))
divider = int(input('Proszę wpisać dowolną liczbę przez którą chcesz podzielić powyższą liczbę: '))

# checking if the inserted number is odd or even and a multiple of 4

if num%2==0 and num%4==0:
    print (f'{num} jest parzysta i podzielna przez 4.')
elif num%2==0:
    print (f'{num} jest parzysta,ale niepodzielna przez 4.')
else:
    print (f'{num} jest nieparzysta.')

if num%divider==0:
    print (f'{num} jest podzielna przez {divider}.')
else:
    print (f'{num} nie jest podzielna przez {divider}.')
    
