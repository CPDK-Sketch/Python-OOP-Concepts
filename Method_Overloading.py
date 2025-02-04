# Understanding Method Overloading in Python

class MathOperations:
    """Demonstrates method overloading using default arguments."""

    def add(self, a, b, c=None):
        """Adds two or three numbers based on parameters provided."""
        if c is None:
            return a + b
        return a + b + c


math_op = MathOperations()
print(math_op.add(2, 3))       # Output: 5
print(math_op.add(2, 3, 4))    # Output: 9
