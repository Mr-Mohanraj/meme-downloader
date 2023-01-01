class Printer:
    def __init__(self):
        self.quotes = []
        self.tags = []
        self.check_data()
        self.print_quotes()

    def check_data(self):
        if self.quotes or self.tags:
            print("assign the value of quotes and tags")
            return False
        else:
            return True

    def print_quotes(self, quotes):
        for quo in quotes:
            print(quo[0])

    def print_tags(self, tags):
        for tag in tags:
            print(tag[0])

    def print_tags_link(self, tags):
        for tag in tags:
            print(f"Tag:{tag[0]}| | Link:{tag[1]}")

    def print_author_about_link(self, tags):
        for quo in quotes:
            print(quo[2])

    def print_values(self, quotes: bool = False, populartags: bool = False):
        if quotes:
            print(self.quotes_with)
        elif populartags:
            print(self.popular_tags)
        else:
            print(self.quotes_with, self.popular_tags)
