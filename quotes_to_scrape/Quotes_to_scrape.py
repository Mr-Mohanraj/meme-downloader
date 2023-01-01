from scraper import Scraper
from to_file import FileSaver
from checker import Checker
from printer import Printer


if __name__ == "__main__":
    da = Scraper()
    da.get_popular_tags_link()
    de.get_quotes()
    p = Printer()
    p.print_quotes()
