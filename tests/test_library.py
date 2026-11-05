
"""
Automated tests for the Library Management System.
Team: DalitechX
"""

import unittest

from book import Book
from library import Library


class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("B001", "Python Basics", "John Smith")

        self.assertEqual(book.book_id, "B001")
        self.assertEqual(book.title, "Python Basics")
        self.assertEqual(book.author, "John Smith")
        self.assertTrue(book.is_available)

    def test_borrow_book(self):
        book = Book("B001", "Python Basics", "John Smith")

        result = book.borrow()

        self.assertTrue(result)
        self.assertFalse(book.is_available)

    def test_return_book(self):
        book = Book("B001", "Python Basics", "John Smith")

        book.borrow()
        result = book.return_book()

        self.assertTrue(result)
        self.assertTrue(book.is_available)


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        result = self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        self.assertEqual(result, "Book successfully added.")
        self.assertEqual(len(self.library.books), 1)

    def test_duplicate_book_id(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        result = self.library.add_book(
            "B001", "Clean Code", "Robert Martin"
        )

        self.assertEqual(result, "Book ID already exists.")
        self.assertEqual(len(self.library.books), 1)

    def test_search_by_id(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        book = self.library.search_by_id("B001")

        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Python Basics")

    def test_search_missing_book(self):
        book = self.library.search_by_id("B999")

        self.assertIsNone(book)

    def test_search_by_title(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        results = self.library.search_by_title("python")

        self.assertEqual(len(results), 1)

    def test_borrow_available_book(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        result = self.library.borrow_book("B001")

        self.assertEqual(result, "Borrowing successful.")
        self.assertFalse(
            self.library.search_by_id("B001").is_available
        )

    def test_borrow_already_borrowed_book(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        self.library.borrow_book("B001")

        result = self.library.borrow_book("B001")

        self.assertEqual(result, "Book is already borrowed.")

    def test_return_borrowed_book(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        self.library.borrow_book("B001")

        result = self.library.return_book("B001")

        self.assertEqual(result, "Book successfully returned.")
        self.assertTrue(
            self.library.search_by_id("B001").is_available
        )

    def test_return_available_book(self):
        self.library.add_book(
            "B001", "Python Basics", "John Smith"
        )

        result = self.library.return_book("B001")

        self.assertEqual(result, "No borrowed book found.")

    def test_borrow_missing_book(self):
        result = self.library.borrow_book("B999")

        self.assertEqual(result, "Book not found.")


if __name__ == "__main__":
    unittest.main()
