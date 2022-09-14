import requests
from bs4 import BeautifulSoup
import time
import os

class Checker:
    
    def __init__(self) -> None:
        pass
    
    def checker(links:list):
        total_page = len(links)
        try:
            for link in links:
                os.system("cls")
                print("Remaining Web pages -->",total_page)
                print(f"Current downloading --> https://tamil.news18.com/photogallery/memes/{link}")
                
                url = f"https://tamil.news18.com/photogallery/memes/{link}"
                url = requests.get(url)
                content = url.content
                soup = BeautifulSoup(content, features="lxml")
                image_links=soup.find_all('div',class_='image-container')
                
                links =[]
                for _ in image_links:
                    links.append(_.img['src'])
                time.sleep(1)
                total_page -= 1
                from image_D import ImageDownloader
                ImageDownloader.download(links)
        except Exception as error:
            print("The error in html_checker.py file -->", error)
