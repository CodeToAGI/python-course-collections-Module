# Library Management System

A simple command-line Library Management System implemented in Python using Object-Oriented Programming (OOP) concepts.

## Features

- **Book Management**: Create books with title and author
- **Library Operations**:
  - Add books to the library
  - Display all books with their status
  - Borrow a book (marks as unavailable)
  - Return a book (marks as available)
- **Status Tracking**: Each book shows "Available" or "Borrowed" status
- **User-Friendly Messages**: Emoji-enhanced console output

## Classes

### Book
- `__init__(self, title, author)`: Initializes a new book
- `borrow()`: Borrows the book if available
- `return_book()`: Returns the book if borrowed
- `__str__()`: String representation of the book

### Library
- `__init__(self)`: Creates an empty library
- `add_book(book)`: Adds a book to the library
- `display_books()`: Shows all books in the library
- `borrow_book(title)`: Borrows a book by title
- `return_book(title)`: Returns a book by title

## How to Run

1. Ensure you have Python 3 installed
2. Save the code as `challenge_solution.py`
3. Run the script:
   ```bash
   python challenge_solution.py
