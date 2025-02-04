class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is not available."

    def return_book(self):
        self.is_available = True
        return f"{self.title} has been returned."

book1 = Book("Python Programming", "John Doe", "123456789")
print(book1.borrow_book())
print(book1.return_book())
