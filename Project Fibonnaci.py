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
    f_seq = []
    for i in range(0,x):
        fib_num0=i
        f_seq.append(fib_num0)
        
        fib_num1=fib_num0
        f_seq.append(fib_num1)
        
        fib_num2=fib_num0 + fib_num1
        f_seq.append(fib_num2)

        fib_num3=fib_num1 + fib_num2
        f_seq.append(fib_num3)

        fib_num4=fib_num2 + fib_num3
        f_seq.append(fib_num3)

        
    
    print(f_seq)

fibonnaci_sq(7)

