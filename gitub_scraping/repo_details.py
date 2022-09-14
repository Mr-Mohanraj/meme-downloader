from bs4 import BeautifulSoup
import requests


class RepoDetails:
    def __init__(self):
        """This class return all Tending values are \
            # Repositories link 
            # Repositories short explain
            # Repositories Total stars
            # Repositories Today stars 
            """
        
        url = "https://github.com/trending/python?since=daily&spoken_language_code=en"
        r = requests.get(url=url)
        self.soup = BeautifulSoup(r.text, 'html.parser')
        self.repo_link()
        self.repo_explain()
        self.repo_stars()
        self.repo_today_stars()
        
    def repo_link(self):
        tending_repo_link = []
        repo = self.soup.find_all('h1', class_="h3 lh-condensed")
        for i in repo:
            value = i.a['href']
            tending_repo_link.append(value)
        return tending_repo_link
        
    def repo_explain(self):
        tending_repo_explain = []
        explain = self.soup.find_all('p',class_="col-9 color-fg-muted my-1 pr-4")
        for i in explain:
            value = i.text.strip()
            tending_repo_explain.append(value)
        return tending_repo_explain
    
    def repo_stars(self):
        tending_repo_stars = []
        stars = self.soup.find_all('div', class_="f6 color-fg-muted mt-2")
        for i in stars:
            value = i.a.text.strip()
            tending_repo_stars.append(value)
        return tending_repo_stars
    
    def repo_today_stars(self):
        tending_repo_todayStars = []
        today_stars = self.soup.find_all('span', class_="d-inline-block float-sm-right")
        for i in today_stars:
            value = i.text.strip()
            tending_repo_todayStars.append(value)
        return tending_repo_todayStars

