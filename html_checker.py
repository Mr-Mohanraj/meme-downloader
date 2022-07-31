import requests
from bs4 import BeautifulSoup
import time
import os

class Checker:
    
    def __init__(self) -> None:
        pass
    
    def checker(links:list):
        try:
            for link in links:
                print("links",link)
                url = f"https://tamil.news18.com/photogallery/memes/{link}"
                url = requests.get(url)
                content = url.content
                soup = BeautifulSoup(content, features="lxml")
                e=soup.find_all('div',class_='image-container')
                links =[]
                for _ in e:
                    links.append(_.img['src'])
                print("html_checker file ->",len(links))
                time.sleep(1)
                from image_D import ImageDownloader
                ImageDownloader.download(links)
                os.system('cls')
        except Exception as error:
            print("The error in html_checker.py file -->", error)
