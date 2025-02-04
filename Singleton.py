# Understanding Singleton Pattern

class Singleton:
    """Ensures only one instance exists."""

    _instance = None  # Private class variable

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True (Both refer to the same instance)
