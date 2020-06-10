# project Euler 4 - largest palindrome of two 3 - digit numbers



palindromes=[]
multiplers = {}
for num1 in range (100,1000):
    for num2 in range (100,1000):
        product = str(num1*num2)
        if len(product)==5:
            if product[0] == product[-1] and product[1] == product[-2] :
                multiplers[product] = (num1, num2)
                product=int(product)
                palindromes.append(product)
                #print(f'{num1} x {num2} = {product}')
        else:
            if product[0] == product[-1] and product[1] == product[-2] and product[2]==product[-3]:
                multiplers[product] = (num1, num2)
                product=int(product)
                palindromes.append(product)
                #print(f'{num1} x {num2} = {product}')

answer = max(palindromes)
print(answer)
print(multiplers['906609'])

# ------------------ other way -------------------------

palindromes1=[]
for num1 in range (100,1000):
    for num2 in range (100,1000):
        product1 = str(num1*num2)
        if product1 == product1[::-1]:
            product1=int(product1)
            palindromes1.append(product1)

answer1 = max(palindromes1)
print(answer1)
