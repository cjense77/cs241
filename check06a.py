class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display(self):
        print("\n{} ({}) by {}".format(self.title,
                                     self.publication_year,
                                     self.author))

class TextBook(Book):

    def __init__(self):
        super().__init__()
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))


class PictureBook(Book):

    def __init__(self):
        super().__init__()
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))

def main():
    b1 = Book()
    b1.prompt_book_info()
    b1.display()
    print()

    tb1 = TextBook()
    tb1.prompt_book_info()
    tb1.prompt_subject()
    tb1.display()
    tb1.display_subject()
    print()

    pb1 = PictureBook()
    pb1.prompt_book_info()
    pb1.prompt_illustrator()
    pb1.display()
    pb1.display_illustrator()

if __name__ == "__main__":
    main()