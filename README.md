
# Library Management System

**Team:** DALITECHX

**Challenge:** 14-Day Python Project Challenge

**Day:** 3

**Level:** Beginner–Intermediate

**Language:** Python

## 1. Project Description

The Library Management System is a command-line Python
application designed to help librarians manage books.

The application allows users to add books, search for books,
borrow available books, return borrowed books and display
all registered books.

The project demonstrates Object-Oriented Programming (OOP)
using Python classes and objects.

## 2. Features

- Add new books.
- Assign unique IDs to books.
- Prevent duplicate book IDs.
- Search books by ID.
- Search books by title.
- Borrow available books.
- Prevent borrowing already borrowed books.
- Return borrowed books.
- Prevent returning books that are not borrowed.
- Display all registered books.
- Menu-driven interface.

## 3. Project Structure

Library-Management-System/

- main.py
- book.py
- library.py
- README.md
- tests/
- ``__init__.py``
  - test_library.py

## 4. Requirements

- Python 3
- Visual Studio Code or another Python editor.

No external Python packages are required.

## 5. Installation

1. Create or download the project folder.
2. Open the folder in VS Code.
3. Open the terminal.
4. Run the application.

## 6. Running the Application

```powershell
python main.py
```

## 7. Running Automated Tests

```powershell
python -m unittest discover -s tests -v
```

## 8. Data Structures Explanation

The project uses a Python list to store multiple Book objects.

Each Book object contains:

- Book ID
- Title
- Author
- Availability status

Classes organize the code while methods perform
operations such as adding, searching, borrowing
and returning books.

## 9. OOP Concepts Practised

- Classes
- Objects
- Attributes
- Methods
- Constructors
- Object state management
- Lists
- Loops
- Conditional statements

## 10. Team

DalitechX

## 11. Learning Outcome

This project demonstrates how Python classes and objects
can be used to model a real-world library management system.

**BUILD. TEST. EXPLAIN.**
