
"""
Main application for the Library Management System.

Team: DalitechX
Day 3 - 14-Day Python Project Challenge
"""

from library import Library


def display_menu():
    """Display the main menu."""

    print("\n====================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add a new book")
    print("2. Search book by ID")
    print("3. Search book by title")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Display all books")
    print("7. Exit")
    print("====================================")


def add_book_prompt(library):
    """Collect information and register a book."""

    print("\n========== ADD NEW BOOK ==========")

    book_id = input("Enter book ID: ").strip()
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    result = library.add_book(book_id, title, author)

    print(f"\n{result}")


def search_book_by_id_prompt(library):
    """Search for a book using its ID."""

    print("\n========== SEARCH BOOK BY ID ==========")

    book_id = input("Enter book ID: ").strip()

    book = library.search_by_id(book_id)

    if book is None:
        print("\nBook not found.")
    else:
        print("\nBook found!")
        book.display_info()


def search_book_by_title_prompt(library):
    """Search for books using their titles."""

    print("\n========== SEARCH BOOK BY TITLE ==========")

    title = input("Enter book title: ").strip()

    books = library.search_by_title(title)

    if not books:
        print("\nBook not found.")
        return

    print(f"\nFound {len(books)} matching book(s):")

    for number, book in enumerate(books, start=1):
        print(f"\nBook {number}")
        book.display_info()


def borrow_book_prompt(library):
    """Borrow a book."""

    print("\n========== BORROW BOOK ==========")

    book_id = input("Enter book ID: ").strip()

    result = library.borrow_book(book_id)

    print(f"\n{result}")


def return_book_prompt(library):
    """Return a borrowed book."""

    print("\n========== RETURN BOOK ==========")

    book_id = input("Enter book ID: ").strip()

    result = library.return_book(book_id)

    print(f"\n{result}")


def main():
    """Run the Library Management System."""

    library = Library()

    print("\nWelcome to DalitechX Library Management System!")

    while True:

        display_menu()

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_book_prompt(library)

        elif choice == "2":
            search_book_by_id_prompt(library)

        elif choice == "3":
            search_book_by_title_prompt(library)

        elif choice == "4":
            borrow_book_prompt(library)

        elif choice == "5":
            return_book_prompt(library)

        elif choice == "6":
            library.display_books()

        elif choice == "7":
            print("\nThank you for using DalitechX Library Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()
