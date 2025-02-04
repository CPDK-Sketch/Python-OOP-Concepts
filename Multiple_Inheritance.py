# Understanding Multiple Inheritance

class Parent1:
    """First parent class."""

    def show_message(self):
        return "Message from Parent1"


class Parent2:
    """Second parent class."""

    def show_another_message(self):
        return "Message from Parent2"


class Child(Parent1, Parent2):
    """Child class inheriting from both Parent1 and Parent2."""
    pass


obj = Child()
print(obj.show_message())        # Output: Message from Parent1
print(obj.show_another_message())# Output: Message from Parent2
