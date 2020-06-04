print('----------------------Project-Crypto---------------------------')


import random, string



task = input("Type 'E' if you wnat to encrypt or 'D' if you want to decrypt")
word = str(input("Type in the secret word: "))
word_new = []
    
keys= string.ascii_lowercase
values = keys[::-1]

code_en=dict(zip(keys, values))

code_de=dict(zip(values, keys))

if task=="e" or task=="E":
    for letter in word:
        letter = code_en[letter]
        word_new.append(letter)
                    
elif task=="d" or task=="D":
    for letter in word:
        letter = code_de[letter]
        word_new.append(letter) 
    
print("".join(word_new))

print('----------------------with compehension---------------------------')

if task=="e" or task=="E":
   word_en = [code_en[letter] for letter in word]
   print("Encrypted word is: " + "".join(word_en))    
            
elif task=="d" or task=="D":
    word_de = [code_de[letter] for letter in word]
    print("Encrypted word is: " + "".join(word_de))
else:
    print('error')


