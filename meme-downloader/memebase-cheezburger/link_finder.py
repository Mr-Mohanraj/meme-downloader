import time
import requests
from bs4 import BeautifulSoup
import os
from image_download import ImageDownloader


class LinkFinder:
    def __init__(self,links:list):
        self.links = list(links)
        self.link_pass(self.links)
        # pass
        
    def link_pass(self, links: list):
        total_page = len(links)
        for i in links:
            os.system('cls')
            print("Remaining Web pages -->",total_page)
            print("current Downloading.. website -->",i) # new website link hold by the i variable
            url = f"{i}"
            r = requests.get(url)
            content = r.content
            soup = BeautifulSoup(content, 'lxml')
            input_ = soup.find_all('img', class_="resp-media lazyload")
            list_link = []
            for i in input_:
                inp = i[r'data-src'] # inside the image tag data-src attribute held the img source link
                list_link.append(inp)
            
            ImageDownloader.download(list_link)
            time.sleep(1)
            total_page -= 1
