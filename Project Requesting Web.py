import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.nytimes.com/")

source=source.text
soup = BeautifulSoup(source, 'html.parser')
#soup=soup.h2

print(soup.find_all('h2'))

