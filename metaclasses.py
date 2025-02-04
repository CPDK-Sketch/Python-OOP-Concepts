# Understanding Metaclasses

class CustomMeta(type):
    """Metaclass that modifies class creation."""

    def __new__(cls, name, bases, dct):
        dct["category"] = "Auto-Generated"  # Adds a new attribute to all instances
        return super().__new__(cls, name, bases, dct)


class Product(metaclass=CustomMeta):
    """Product class using a metaclass."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


item = Product("Laptop", 1000)
print(item.category)  # Output: Auto-Generated
