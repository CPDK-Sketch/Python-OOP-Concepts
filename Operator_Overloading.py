# Understanding Operator Overloading

class Money:
    """Demonstrates overloading arithmetic operators."""

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        """Overloads the + operator."""
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"


wallet1 = Money(500)
wallet2 = Money(300)
total_wallet = wallet1 + wallet2  # Using overloaded + operator
print(total_wallet)  # Output: ₹800
