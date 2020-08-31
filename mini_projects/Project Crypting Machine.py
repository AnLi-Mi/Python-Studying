print('----------------------Project-Crypto---------------------------')
# Creating an encrypting or decrypting (depenading on the usre's request) machine
# that replaces each letter of given string with a letter with the same index in
# the rotated alphabet (zyxwu...)

import random, string


#asking user to choose if they want to encode or decode
task = input("Type 'E' if you wnat to encrypt or 'D' if you want to decrypt")
#asking user to input the messange they want to encrypt/decrypt
word = str(input("Type in the secret word: "))
word_new = []

# creating a string of the alphabet letter to use in the crypting machine    
keys= string.ascii_lowercase
# creating a string of the roteated alphabet letter to use in the crypting machine
values = keys[::-1]

# actual code of the encoding machine replacing letters
code_en=dict(zip(keys, values))
# actual code of the decoding machine replacing letters
code_de=dict(zip(values, keys))

# executing the replacing code and putting the replaced latters together into a new word
if task=="e" or task=="E":
    for letter in word:
        letter = code_en[letter]
        word_new.append(letter)
                    
elif task=="d" or task=="D":
    for letter in word:
        letter = code_de[letter]
        word_new.append(letter)

#printing the result as a whole word    
print("".join(word_new))

print('----------------------solution with compehension---------------------------')

if task=="e" or task=="E":
   word_en = [code_en[letter] for letter in word]
   print("Encrypted word is: " + "".join(word_en))    
            
elif task=="d" or task=="D":
    word_de = [code_de[letter] for letter in word]
    print("Encrypted word is: " + "".join(word_de))
else:
    print('error')


