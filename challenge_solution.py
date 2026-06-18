class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"✅ '{self.title}' has been borrowed.")
        else:
            print(f"❌ '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"✅ '{self.title}' has been returned.")
        else:
            print(f"ℹ️ '{self.title}' was not borrowed.")

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"📚 Added: {book.title}")

    def display_books(self):
        print("\n===== LIBRARY BOOKS =====")

        if not self.books:
            print("No books in library.")
            return

        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return

        print("❌ Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return

        print("❌ Book not found.")


# =====================
# Main Program
# =====================

library = Library()

book1 = Book("Python Basics", "Mahaz Abbasi")
book2 = Book("Learn OOP", "CodeToAGI")
book3 = Book("AI Fundamentals", "OpenAI")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

print("\n--- Borrowing a Book ---")
library.borrow_book("Python Basics")

library.display_books()

print("\n--- Returning a Book ---")
library.return_book("Python Basics")

library.display_books()
