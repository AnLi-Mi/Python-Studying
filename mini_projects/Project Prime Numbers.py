#Ask the user for a number and determine whether the number is prime or not.
#Take this opportunity to practice using functions, described below.

# --------------------------SOLUTION-------------------------------

def get_num(request):
    return int(input(request))

def prime(x):
    div=[]
    for i in range(1, x+1):
        if x%i==0:
            div.append(i)
    if len(div)==2 or len(div)==2:
        print (f'{x} jest liczbą pierwszą')
    else:
        print (f'{x} nie jest liczbą pierwszą')
    return x, div

num=get_num("Proszę podać liczbę by sprawdzić czy jest ona liczbą pierwszą: ")
prime(num)
