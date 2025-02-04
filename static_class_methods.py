# Static Methods & Class Methods

class MathOperations:
    count = 0  # Class variable

    def __init__(self, value):
        self.value = value
        MathOperations.count += 1

    @staticmethod
    def add(a, b):
        """Static method: No access to class or instance attributes."""
        return a + b

    @classmethod
    def get_instance_count(cls):
        """Class method: Accesses class variables."""
        return f"Total instances created: {cls.count}"


obj1 = MathOperations(10)
obj2 = MathOperations(20)

print(MathOperations.add(5, 10))  # Output: 15
print(MathOperations.get_instance_count())  # Output: Total instances created: 2
