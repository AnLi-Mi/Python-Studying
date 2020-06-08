import random

x = int(input("Choose number of prectice questions"))
i=1
r=0

while i < x+1:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"{a} x {b} = ")
    ans = int(input("wynik: "))
    if ans == a*b:
        r+=1
    i+=1

result=round(r/x*100, 2)
print ('Thank you for playing!')
print (f'You hve managed to have {r} correct answers')
print (f'Your test result is {result}%')
    
        
