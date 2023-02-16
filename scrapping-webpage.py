#Import the libraries

import requests
from bs4 import BeautifulSoup

#Get the website HTML

website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

#We can use the following code to find that box
box = soup.find('article', class_='main-article')

#To get Tiltle

title = box.find('h1').get_text()
# print(title)

transcript = box.find('div', class_='full-script')
transcript = transcript.get_text(strip=True, separator=' ')
# print(transcript)

#Export data into a text file

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

#Scrape Multiple Web Pages

root = 'https://subslikescript.com/movies'
website = f'{root}/movies'

box.find_all('a', href=True)

for link in box.find_all('a', href = True):
    link['href']

links = [link['href'] for link in box.find_all('a', href=True)]
print(links)

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')





