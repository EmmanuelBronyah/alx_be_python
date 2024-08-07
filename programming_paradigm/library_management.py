class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = not self._is_checked_out

    def return_book(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()

    def list_available_books(self):
        for book in self._books:
          if book._is_checked_out == True:
            continue
          print(book.return_book())
