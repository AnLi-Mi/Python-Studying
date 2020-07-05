#Write a program that asks the user how many Fibonnaci numbers to generate
#and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence
#to generate.
#Hint: The Fibonnaci seqence is a sequence of numbers where
#the next number in the sequence is the sum of the previous two numbers
#in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


# ------------------------SOLUTION -----------------------------

#rquesting user for telling how many Fibonnaci numbers to generate

num = int(input("How many Fibonnaci numbers would you like to generate?: "))

def fibonnaci_sq(x):
    f_seq = [1]
    fib_num=f_seq[0] + f_seq[0]-1
    f_seq.append(fib_num)
    for i in range(1,x-1):
        fib_num=f_seq[i] + f_seq[i-1]
        f_seq.append(fib_num)
        
    print(f_seq)

fibonnaci_sq(num)





 


