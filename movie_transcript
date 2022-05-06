"""
asks a url from you and gives you back a .txt file containing the movie full transcript.
the file name is the title of movie
"""
# import neccessary libraries
import requests
from bs4 import BeautifulSoup

# get url from you 
website = input("Please insert your movie's url from subslikescript.com: ")
result = requests.get(website)
content = result.text


soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
