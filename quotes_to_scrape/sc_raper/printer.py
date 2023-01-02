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

    def print_quotes(self):
        for quo in self.quotes:
            print(f"Quotes=>{quo[0]}\n Author=> {quo[1]}")

    def print_tags(self):
        for tag in self.tags:
            print("Popular Tags => ", tag[0])

    def print_tags_link(self):
        for tag in self.tags:
            print(f"Tag:{tag[0]}| | Link:{tag[1]}")

    def print_author_about_link(self):
        for quo in self.quotes:
            print(quo[2])

    def print_values(self, quotes: bool = False, populartags: bool = False):
        if quotes:
            print(self.quotes)
        elif populartags:
            print(self.tags)
        else:
            print(self.quotes, self.tags)
