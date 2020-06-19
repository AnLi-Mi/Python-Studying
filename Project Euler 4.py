 # project Euler 4 - largest palindrome which is a product of two 3 - digit numbers

import time

print ('------------------ my ogiginal way -------------------------')
start_time = time.time()
palindromes=[]
#multiplers = []
tests=0
for num1 in range (100,1000):
    for num2 in range (100,1000):
        tests+=1
        product = str(num1*num2)
        if len(product)==5:
            if product[0] == product[-1] and product[1] == product[-2] :
#                multiplers.append(f'{num1} x {num2} = {product}')
                product=int(product)
                palindromes.append(product)
                #print(f'{num1} x {num2} = {product}')
            if num1==num2:
                break
        else:
            if product[0] == product[-1] and product[1] == product[-2] and product[2]==product[-3]:
                #multiplers[product] = (num1, num2)
                product=int(product)
                palindromes.append(product)
                #print(f'{num1} x {num2} = {product}')
            if num1==num2:
                break

answer = max(palindromes)
print(answer)
#print(multiplers)
print(tests)
end_time=time.time()
print(f'time = {end_time - start_time}')

print('---------------------- other way ----------------------------')
start_time1 = time.time()
palindromes1=[]
for num1 in range (100,1000):
    for num2 in range (100,1000):
        tests+=1
        product1 = str(num1*num2)
        if product1 == product1[::-1]:
            product1=int(product1)
            palindromes1.append(product1)
        if num1==num2:
            break

answer1 = max(palindromes1)
print(answer1)
#print(multiplers['906609'])
print (tests)
end_time1=time.time()
print(f'time1 = {end_time1 - start_time1}')

print('----------------------starting from the highest numbers-----------')

def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return (True)
    else:
        return (False)

def palindrom():
    start = time.time()
    palindromes = []
    multiplers = []
    tests=0
    low_range=99
    high_range=999
    low_range2=99
    for num1 in range (high_range,low_range,-1):
        for num2 in range (high_range, low_range2, -1):
            tests+=1
            product = str(num1*num2)
            #print(num1, num2)
            if is_palindrome(product):
                product=int(product)
                palindromes.append(product)
            
                multiplers.append([num1, num2, product])
            if num1 == num2:
               break
        
    
    print(max(palindromes))
    print(tests)
    #print(multiplers)
    end = time.time()
    print(round((end - start),2))

palindrom()

print ('----------------------starting from palindrome-----------------------')
import time

def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return (True)
    else:
        return (False)


start=time.time()
t=0
b= False
for i in range (998001, 10000, -1):
        t+=1
        if is_palindrome(i):
            
            for x in range(999, 99, -1):
             
                if i%x==0  and i/x in range (99, 999):
                    print(f'{x} x {i/x} = {i}')
                    
                    b=True
                    break
                
        if b==True:
            break
                  
            
        
end=time.time()               
print(t)
print(round((end-start),2))

