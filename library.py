
"""
Library class for managing book collections.
Team: Nexora
"""

from book import Book


class Library:
    """Manages all books in the library."""

    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        """Add a new book to the library."""

        book_id = str(book_id).strip()
        title = title.strip()
        author = author.strip()

        if not book_id or not title or not author:
            return "Book ID, title and author are required."

        if self.search_by_id(book_id):
            return "Book ID already exists."

        new_book = Book(book_id, title, author)

        self.books.append(new_book)

        return "Book successfully added."

    def search_by_id(self, book_id):
        """Find a book using its ID."""

        book_id = str(book_id).strip()

        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def search_by_title(self, title):
        """Search for books using their titles."""

        title = title.strip().lower()

        if not title:
            return []

        matching_books = []

        for book in self.books:
            if title in book.title.lower():
                matching_books.append(book)

        return matching_books

    def borrow_book(self, book_id):
        """Borrow a book if it is available."""

        book = self.search_by_id(book_id)

        if book is None:
            return "Book not found."

        if not book.is_available:
            return "Book is already borrowed."

        book.borrow()

        return "Borrowing successful."

    def return_book(self, book_id):
        """Return a previously borrowed book."""

        book = self.search_by_id(book_id)

        if book is None:
            return "Book not found."

        if book.is_available:
            return "No borrowed book found."

        book.return_book()

        return "Book successfully returned."

    def display_books(self):
        """Display all registered books."""

        if not self.books:
            print("No books registered in the library.")
            return

        print("\n========== LIBRARY BOOKS ==========")

        for number, book in enumerate(self.books, start=1):
            print(f"\nBook {number}")
            book.display_info()

        print("\n===================================")
