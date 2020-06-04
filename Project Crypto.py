print('----------------------Project-Crypto---------------------------')


import random, string

task = input("Type 'E' if you wnat to encrypt or 'D' if you want to decrypt")
word = str(input("Type in the secret word: "))
word_en = []
word_de = []


keys= string.ascii_lowercase
values = keys[::-1]

code_en=dict(zip(keys, values))

code_de=dict(zip(values, keys))

if task=="e" or task=="E":
   for letter in word:
       letter = code_en[letter]
       word_en.append(letter)
   print("Encrypted word is: " + "".join(word_en))    
            
elif task=="d" or task=="D":
    for letter in word:
       letter = code_de[letter]
       word_de.append(letter)
    print("Decrypted word is: " + "".join(word_de))
else:
    print('error')




