import requests
from link_finder import LinkFinder
from bs4 import BeautifulSoup

# this download method only work on the this side only
# https://memebase.cheezburger.com/ this side home content only downloadable 

url = "https://memebase.cheezburger.com/"
r = requests.get(url) # get request file from the website
content = r.content # get content of the file <html> template file

soup = BeautifulSoup(content, 'lxml')
input_ = soup.find_all('div', class_="mu-view-post mu-section") # find the div tags with particular class name

list_link = []
for i in input_:
    links = i.a['href'] # inside the div <a href="link"> 
    list_link.append(links)

print("list of meme site in memebase-cheezburger website -->",len(list_link))

LinkFinder(list_link) # find the source of the image file inside in website
