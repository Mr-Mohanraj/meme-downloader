import requests
from bs4 import BeautifulSoup
import csv


url2 = "https://quotes.toscrape.com/tag/love/page/2/"
url3 = "https://quotes.toscrape.com/tag/love/page/3/"


# URL = "https://quotes.toscrape.com/"

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
        print(url in "https://quotes.toscrape.com/")
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

    def change_url_popular_tag(tags: list, select_tag: int = 0):
        """This function return a url based on the popular urls"""
        print("Today popular tags and links:" + '\n' + tags)
        url = "https://quotes.toscrape.com" + tags[select_tags]['taglink']
        return url

    def print_values(self, quotes: bool = False, populartags: bool = False):
        if quotes:
            print(self.quotes_with)
        elif populartags:
            print(self.popular_tags)
        else:
            print(self.quotes_with, self.popular_tags)

    def check_next_page(self):
        if "No quotes found!" in self.soup.select('div.col-md-8')[1].text.strip():
            return False
        else:
            return True

    def next_page(tagname: str = 'love', pagenum: int = 1):
        """
        tagname like "love", pagenum like 1,2,3
        """
        return f"https://quotes.toscrape.com/tag/{tagname}/page/{pagenum}/"

    def privious_page(self, page_num: int):
        """Page_num 0 = 1,1 = 2,2 = 3...."""
        if page_num <= 0:
            page_url = f"https://quotes.toscrape.com/tag/{current_tag_name}"
        else:
            page_url = f"https://quotes.toscrape.com/tag/{current_tag_name}/page/{page_num}/"
        return page_url

    def to_csv_file(self, quotes_with):

        fileds = ["Quotes", "Author", "About Author",
                  "popular_tags", "link Popular"]

        with open('filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fileds)
            for i in self.quotes_with:
                writer.writerow(i)

    def extends_quotes(self):
        for tags, quotes in zip(popular_tags, quotes_with):
            quotes.extend(tags)


if __name__ == "__main__":
    da = Scraper(url="https://quotes.toscrape.com/tag/deep-thoughts/page/1/")
    print(da.url)
