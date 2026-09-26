class Book:
    def __init__(self, title):
        self.title = title


class SearchService:
    def search(self, book_name):
        print("Searching for:", book_name)


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("C Programming")
        ]

    def search_book(self, search_service, book_name):
        search_service.search(book_name)


library = Library()
search_service = SearchService()

library.search_book(search_service, "Python")