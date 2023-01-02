class Checker:
    def __init__(self):
        self.current_tag_name = "love"

    # def change_url_popular_tag(self, tags: list, select_tag: int = 0):
    #     """This function return an url based on the popular urls"""
    #     return "https://quotes.toscrape.com" + tags[select_tag]["taglink"]

    @staticmethod
    def check_quotes_page(soup: object):
        """Next page is there or not. with help to find the page have a quotes or not \
           based on the "No Quotes found"
        """
        if "No quotes found!" in soup.select('div.col-md-8')[1].text.strip():
            return False
        else:
            return True

    def next_page(self, pagenum: int = 1):
        """
        tagname like "love", pagenum like 1,2,3
        """
        return f"https://quotes.toscrape.com/tag/{self.current_tag_name}/page/{pagenum}/"

    def privious_page(self, page_num: int):
        """Page_num 0 = 1,1 = 2,2 = 3...."""
        if page_num <= 0:
            page_url = f"https://quotes.toscrape.com/tag/{self.current_tag_name}"
        else:
            page_url = f"https://quotes.toscrape.com/tag/{self.current_tag_name}/page/{page_num}/"

        return page_url
