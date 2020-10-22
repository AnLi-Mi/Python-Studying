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

def calendar (a,b,c,d,e,f,g,h,i,j,k,l, year):
    print (f'{a}, {c}, {e}, {g}, {h}, {j}, {l}, have 31 days')


calendar(*months, year=2020)




