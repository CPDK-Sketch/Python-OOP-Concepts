# Composition & Aggregation

class Engine:
    """Engine class with its own properties."""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started."


class Car:
    """Car class that 'has-a' Engine (Composition)."""

    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # Composition

    def start_car(self):
        return f"{self.brand} car: {self.engine.start()} with {self.engine.horsepower} HP"


my_car = Car("Tesla", 500)
print(my_car.start_car())  # Output: Tesla car: Engine started. with 500 HP
