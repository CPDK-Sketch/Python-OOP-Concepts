
# Understanding Abstraction
""" to concentrate on the core functionality of an object without getting entangled in the intricacies of its implementation. 
Python's abc module (Abstract Base Classes) takes this a step further by enabling to define abstract base classes. 
These classes serve as blueprints for other classes, outlining essential methods that concrete subclasses must implement."""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract class that forces subclasses to implement start() method."""

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        """Concrete method (not abstract)."""
        print("Vehicle stopped.")

class Car(Vehicle):
    """Car class implementing the start() method."""

    def start(self):
        print("Car engine started.")

# car = Vehicle()  # ❌ ERROR: Cannot instantiate an abstract class
car = Car()  # ✅ Works because Car implements start()
car.start()  # Output: Car engine started.
car.stop()   # Output: Vehicle stopped.
