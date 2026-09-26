class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book:", self.title)


class Library:
    def __init__(self):
        self.books = [
            Book("Python Programming"),
            Book("Java Programming"),
            Book("Data Structures")
        ]

    def display_books(self):
        for book in self.books:
            book.display()


library = Library()
library.display_books()