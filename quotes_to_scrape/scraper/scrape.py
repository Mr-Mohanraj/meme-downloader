import requests
from bs4 import BeautifulSoup
import csv


class Scraper:

    def __init__(self,
                 url="https://quotes.toscrape.com/"
                 ):
        self.url = self.set_url(url)
        res = requests.get(url)
        self.soup = BeautifulSoup(res.content, 'html.parser')
        self.popular_tags = []
        self.quotes_with = []

    def set_url(self, url):
        """
        This function check url is "https://quotes.toscrape.com/"
        """

        if url in "https://quotes.toscrape.com/":
            return url
        else:
            raise Exception(
                "This class only for 'https://quotes.toscrape.com/' website only !!")

    def get_quotes(self):
        all_data = self.soup.select("div.quote")
        for tag in all_data:
            actually_quote = tag.select_one("span.text").text.strip()
            author = tag.select_one("small.author")
            about_author_link = author.fetchNextSiblings()[0]['href'].strip()
            author = author.text.strip()
            self.quotes_with.append(
                [actually_quote, author, "https://quotes.toscrape.com" + about_author_link])
        return self.quotes_with

    def get_popular_tags_link(self):
        tags_items = soup.select("span.tag-item")
        for num in range(len(tags_items)):
            tag_name = tags_items[num].text.strip()
            tag_link = tags_items[num].findChildren()[0]['href'].strip()
            self.popular_tags.append(
                [tag_name, "https://quotes.toscrape.com" + tag_link])
        return self.popular_tags

    def extends_quotes(self):
        for tags, quotes in zip(self.popular_tags, self.quotes_with):
            quotes.extend(tags)
