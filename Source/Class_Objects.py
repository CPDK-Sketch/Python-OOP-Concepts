# class_objects.py - Understanding Classes and Objects

class Car:
    """A simple class representing a Car."""

    def __init__(self, brand, model, year):
        """Constructor: Initializes the car attributes."""
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Returns car details as a string."""
        return f"{self.year} {self.brand} {self.model}"


# Creating objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Display output
print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2022 Honda Civic
