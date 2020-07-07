import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.nytimes.com/")

source=source.text
soup = BeautifulSoup(source, 'html.parser')
#soup=soup.h2

i=1
for header in soup.find_all('h2'):
    print(f"Title {i}: '{header.string}'")
    i+=1

