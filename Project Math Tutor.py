import random

x = int(input("Choose number of prectice questions"))
i=1

while i < x+1:
    a = 3 #tu bedzie losowa liczba
    b = 4 #tu bedzie losowa liczba
    print(f"{a} x {b} = ")
    ans = int(input("wynik: "))
    if ans == a*b:
        print("Dobrze")
    else:
        print("Zle")

    i+=1
    
        
