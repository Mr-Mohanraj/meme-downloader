from sc_raper.scrape import Scraper
from sc_raper.printer import Printer
from sc_raper.to_file import to_csv_file,to_sqlite_file
from sc_raper.checker import Checker


if __name__ == "__main__":
    da = Scraper()
    da.get_popular_tags_link()
    da.get_quotes()
    da.extends_quotes()
    to_csv_file(da.quotes_with)
    p = Printer()
    p.quotes = da.quotes_with
    p.tags = da.popular_tags
    # create_sqlite_file(filename='quotes')
    to_sqlite_file(da.quotes_with)
    check = Checker()

    # print(da.quotes_with)
    count = 0
    for i in da.popular_tags:
        count += 1
        if "https://quotes.toscrape.com/" in i[1]:
            da.set_url(i[1])
        else:
            while True:
                num = 0
                check.current_tag_name = i[0]
                da.set_url(check.next_page(pagenum=count))
                if Checker.check_quotes_page(da.soup):
                    num += 1
                    da.get_quotes()
                    da.get_all_tags_link()
                    da.get_all_tags()
