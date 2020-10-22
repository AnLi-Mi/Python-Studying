# positional arguments

# Ex 1
def months_print(*args, year):
    for arg in args:
        print(f"{arg} {year}")



months = ["jen","feb","mar", "apr", "may", "jun", "jul", "aug", "sept", "oct", "nov", "dec"]


months_print(*months, year='2020')


months_print("jen", "feb", "mar", "april", year='is in spring')

# Ex 2

def multiply(*args):
    total=1
    for arg in args:
        total = total*arg
    return total    


print(multiply(1,3,5,7,9))


# deconstructing arguments

def calendar (a,b,c,d,e,f,g,h,i,j,k,l, year=2020):
    print (f'{a}, {c}, {e}, {g}, {h}, {j}, {l}, have 31 days')


calendar(*months, year=2020)

# arguments that are keys or values of a dictionary

def calendar2(a,b,c,d,e,f,g,h,i,j,k,l):
    print(a,b,c,d,e,f,g,h,i,j,k,l)

months = {"a":31,"b":"28/29","c":31, "d":30, "e":31, "f":30, "g":31, "h":31, "i":30, "j":31, "k":30, "l":31}

calendar2(*months)
calendar2(**months)


