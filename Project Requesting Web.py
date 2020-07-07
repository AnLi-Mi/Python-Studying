import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

a = requests.get(url)

a=a.text
b=BeautifulSoup(a, 'html.parser')
b=b.h2

print(b)

