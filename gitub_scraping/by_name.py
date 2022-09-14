import requests
from bs4 import BeautifulSoup
import re

def valid_username(username):
    """Extract Username from github url """
    if username.startswith('https://github.com/') and (username.find("?") > 0):
        username = username.split('?')[0]
        return username.split('/')[3]
    elif username.startswith('https://github.com/'):
        return username.split('/')[3]


def scraper():
    session = requests.Session()
    url = 'https://github.com/{}'
    username = input("Enter your Github Profile name Here Or github Url(only) : ").strip()
    username = valid_username(username)
    
    r = session.get(url.format(username), params={'page': 1, 'tab': 'repositories'})
    html_soup = BeautifulSoup(r.text, 'html.parser')
    
    repos_element = html_soup.find(id='user-repositories-list')
    
    if repos_element == None:
        print(f"Enter Correct user name here, Check this your username {username}")
    else:
        print("Your name is ",html_soup.find(class_='p-name').get_text(strip=True))
    
    repos = repos_element.find_all('li')
    print(" Repo-Name | programming-language | Stars ")
    
    for repo in repos:
        name = repo.find('h3').find('a').get_text(strip=True)
        language = repo.find(attrs={'itemprop': 'programmingLanguage'})
        language = language.get_text(strip=True) if language else 'unknown'
        stars = repo.find('a', attrs={'href': re.compile('\/stargazers')})
        stars = int(stars.get_text(strip=True).replace(',', '')) if stars else 0
        
        print(f" {name}, {language}, {stars}")


if __name__ == '__main__':
    scraper()