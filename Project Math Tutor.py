import random
from time import time as t


x = int(input("Choose number of prectice questions"))
od = int(input("Choose the begging of the number range"))
do = int(input("Choose the end of the number range"))
i=1
r=0

start = t()

while i < x+1:
    a = random.randint(od, do)
    b = random.randint(od, do)
    prod = a*b
    print(f"{a} x {b} = ")
    ans = int(input("wynik: "))
    if ans == prod:
        r+=1
    i+=1
end=t()
result=round(r/x*100, 2)
print ('Thank you for playing!')
print (f'You have managed to have {r} correct answers')
print (f'Your test result is {result}%')
print (f'It took you {round(end-start,1)} seconds, which is {round((end-start)/x,1)} seconds per question.')

    
        
