from scraper import extend_quotes
class FileSaver:

    def __init__(self):
        self.quotes = extend_quotes()
        self.to_csv_file(self.quotes)


    def to_csv_file(self, quotes):

        fileds = ["Quotes", "Author", "About Author",
                  "popular_tags", "link Popular"]

        with open('filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fileds)
            for i in self.quotes:
                writer.writerow(i)


