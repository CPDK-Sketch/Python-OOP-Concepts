# Understanding Magic Methods (__str__, __len__, __add__)

class Book:
    """Demonstrates magic methods."""

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """Controls what is displayed when print() is used."""
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        """Returns the number of pages."""
        return self.pages

    def __add__(self, other):
        """Allows adding two Book objects to get total pages."""
        return self.pages + other.pages


book1 = Book("Python 101", 300)
book2 = Book("Advanced Python", 400)

print(book1)         # Output: Book: Python 101, Pages: 300
print(len(book1))    # Output: 300
print(book1 + book2) # Output: 700
