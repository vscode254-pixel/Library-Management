
"""
Book class for the Library Management System.
Team: DalitechX
"""


class Book:
    """Represents an individual book in the library."""

    def __init__(self, book_id, title, author):
        self.book_id = str(book_id).strip()
        self.title = title.strip()
        self.author = author.strip()
        self.is_available = True

    def borrow(self):
        """Mark the book as borrowed."""

        if not self.is_available:
            return False

        self.is_available = False
        return True

    def return_book(self):
        """Mark the book as available."""

        if self.is_available:
            return False

        self.is_available = True
        return True

    def display_info(self):
        """Display book information."""

        status = "Available" if self.is_available else "Borrowed"

        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

    def __str__(self):
        """Return a readable representation of the book."""

        status = "Available" if self.is_available else "Borrowed"

        return (
            f"{self.book_id} | {self.title} | "
            f"{self.author} | {status}"
        )
