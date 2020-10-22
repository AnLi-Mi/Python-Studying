def months_print(*args, year):
    for arg in args:
        print(f"It's {arg} {year}")



months = ["jen","feb","mar", "apr", "may", "jun", "jul", "aug", "sept", "oct", "nov", "dec"]


months_print(*months, year='2020')


