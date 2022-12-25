import requests
from bs4 import BeautifulSoup

 
url = "https://quotes.toscrape.com/"
url2 = "https://quotes.toscrape.com/tag/love/page/2/"
url3= "https://quotes.toscrape.com/tag/love/page/3/"

res = requests.get(url)

 
soup = BeautifulSoup(res.content,'lxml')
popular_tags = []
quotes_with = []
 
def get_quotes():
    all_data = soup.select("div.quote")   
    for tag in all_data:
        actually_quote = tag.select_one("span.text").text.strip()
        author = tag.select_one("small.author")
        about_author_link = author.fetchNextSiblings()[0]['href'].strip()
        author = author.text.strip()
        quotes_with.append([actually_quote,author,"https://quotes.toscrape.com"+about_author_link])
    return quotes_with
 
def get_popular_tags_link():
    tags_items = soup.select("span.tag-item")
    for num in range(len(tags_items)):
        tag_name = tags_items[num].text.strip()
        tag_link = tags_items[num].findChildren()[0]['href'].strip()
        popular_tags.append([tag_name,"https://quotes.toscrape.com"+tag_link])
    return popular_tags

 
def change_url_popular_tag(tags:list,select_tag:int = 0):
    """This function return a url based on the popular urls"""
    print("Today popular tags and links:"+'\n'+ popular_tags)
    url = "https://quotes.toscrape.com"+tags[select_tags]['taglink']
    return url

def print_values(quotes:bool = False, populartags:bool = False ):
    if quotes:
        print(quotes_with)
    elif populartags:
        print(popular_tags)
    else:
        print(quotes_with,popular_tags)

def check_next_page():
    if "No quotes found!" in soup.select('div.col-md-8')[1].text.strip():
        return False
    else:
        return True
    
def next_page(tagname:str = 'love', pagenum:int = 1):
    page_url = f"https://quotes.toscrape.com/tag/{tagname}/page/{pagenum}/"
    return page_url

def privious_page(page_num:int):
    """Page_num 0 = 1,1 = 2,2 = 3...."""
    print(page_num)
    if page_num  <= 0:
        page_url = f"https://quotes.toscrape.com/tag/{current_tag_name}"
    else:
        page_url = f"https://quotes.toscrape.com/tag/{current_tag_name}/page/{page_num}/"
    return page_url


def to_csv_file(quotes_with):
    import csv

    fileds = ["Quotes","Author","About Author","popular_tags","link Popular"]

    with open('filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fileds)
        for i in quotes_with:
            writer.writerow(i)
    
get_quotes()
get_popular_tags_link()
for i,j in zip(popular_tags,quotes_with):
    j.extend(i)


to_csv_file(quotes_with)