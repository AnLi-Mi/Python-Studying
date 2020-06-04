print('----------------------Project-Crypto---------------------------')


import random, string

task = input("Type 'en' if you wnat to encrypt or 'de' if you want to decrypt")
word = str(input("Type in the word"))
#word_en = []
#word_de = []

#if en==true:
 #   for sign in word:
        #sposob enkrypcji
  #      word_en.append(sign)
   # print(''.join.word_en())
#else:
 #   for sign in word:
        #odwrocony sposob enkrypcji
  #      word_en.append(sign)
   # print(''.join.word_de())

print('-------------------------------------------------')

       
if task=="en":
    #word.replace("a", "b")
    #word.replace("c", "d")
    #word.replace("e", "f")
    print(word.replace("a", "b"))
elif task=="de":
    #word.replace("b", "a")
    #word.replace("d", "c")
    #word.replace("f", "e")
    print(word.replace("b", "a"))
else:
    print('error')

