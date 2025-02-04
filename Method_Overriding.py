# Understanding Method Overriding

class Parent:
    """Parent class with a generic method."""

    def show_message(self):
        return "Message from Parent class."


class Child(Parent):
    """Child class overrides the show_message() method."""

    def show_message(self):
        return "Message from Child class."


obj = Child()
print(obj.show_message())  # Output: Message from Child class.
