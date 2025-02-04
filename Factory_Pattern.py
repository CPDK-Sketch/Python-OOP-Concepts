# Understanding Factory Pattern

class Animal:
    """Animal Factory"""

    def speak(self):
        pass


class Dog(Animal):
    """Dog subclass"""

    def speak(self):
        return "Bark!"


class Cat(Animal):
    """Cat subclass"""

    def speak(self):
        return "Meow!"


class AnimalFactory:
    """Factory class to create objects"""

    @staticmethod
    def get_animal(animal_type):
        animals = {"dog": Dog(), "cat": Cat()}
        return animals.get(animal_type.lower(), None)


dog = AnimalFactory.get_animal("dog")
print(dog.speak())  # Output: Bark!

cat = AnimalFactory.get_animal("cat")
print(cat.speak())  # Output: Meow!
