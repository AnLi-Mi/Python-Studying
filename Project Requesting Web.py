
# Use the BeautifulSoup and requests Python packages to print out
#a list of all the article titles on the New York Times homepage.

#-------------------SOLUTION----------------

import requests
from bs4 import BeautifulSoup

#downloading the webpage
source = requests.get("https://www.nytimes.com/")


#turning the code into a simple text
source=source.text

#structuring the text the bs
soup = BeautifulSoup(source, 'html.parser')

#starting numbering the listed titles
i=1

#selecting all text that is h2 -> a title of article
for header in soup.find_all('h2'):
    print(f"Title {i}: '{header.string}'")
    i+=1

