print('----------------------Project-Crypto---------------------------')


import random, string

task = input("Type 'en' if you wnat to encrypt or 'de' if you want to decrypt")
word = str(input("Type in the word"))
word_en = []
word_de = []


keys= string.ascii_lowercase
values = keys[::-1]

print(keys)
print(values)

code_en=dict(zip(keys, values))
print(code_en)

code_de=dict(zip(values, keys))
print(code_de)

#if task=="en":
#   for letter in word:
#       if letter == code_en(keys): 
#           letter=conde_en(values)
            
#elif task=="de":
#else:
#print('error')


