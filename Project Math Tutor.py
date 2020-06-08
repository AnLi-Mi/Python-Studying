import random
from time import time as t


x = int(input("Choose number of prectice questions: "))
do = int(input("Choose the highest number for your practice: "))
i=1
r=0

answers=[]

start = t()

while i < x+1:
    a = random.randint(1, do)
    b = random.randint(1, do)
    prod = a*b
    ans = int(input(f"{a} x {b} = "))
    answers.append(f'{a} x {b} = {prod}, your answer: {ans}')
    if ans == prod:
        r+=1
    i+=1
end=t()
result=round(r/x*100, 2)

print ('Thank you for playing!')
print (f'You have managed to have {r} correct answers')
print (f'Your test result is {result}%')
print (f'It took you {round(end-start,1)} seconds, which is {round((end-start)/x,1)} seconds per question.')
for a in answers:
    print(a)
        
