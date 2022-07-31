from bs4 import BeautifulSoup
import requests
try:
    url = "https://tamil.news18.com/photogallery/memes/"

    url = requests.get(url)

    content = url.content

    soup = BeautifulSoup(content, features="lxml")

    e=soup.find_all('div',class_='imgtext')

    links = []
    for _ in e:
        links.append(_.figure.a['href'])
    
    print("download file ->",len(links))
    from html_checker import Checker
    Checker.checker(links=links)
except Exception as error:
    print("The error in download.py file -->", error)