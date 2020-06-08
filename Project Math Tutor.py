import random

x = int(input("Choose number of prectice questions"))
i=1

while i < x+1:
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    print(f"{a} x {b} = ")
    ans = int(input("wynik: "))
    if ans == a*b:
        print("Dobrze")
    else:
        print("Zle")

    i+=1
    
        
