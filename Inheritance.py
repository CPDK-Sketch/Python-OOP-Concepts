#inheritance.py - Understanding Inheritance

class Vehicle:
    """Base class representing a vehicle."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle):
    """Derived class inheriting from Vehicle."""

    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  # Calling parent constructor
        self.fuel_type = fuel_type

    def display_info(self):
        return f"{super().display_info()}, Fuel Type: {self.fuel_type}"


# Creating an object
car = Car("Tesla", "Model S", "Electric")
print(car.display_info())  # Output: Brand: Tesla, Model: Model S, Fuel Type: Electric
