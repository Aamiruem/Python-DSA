# Class: A blueprint for creating objects.
# Object: An instance of a class.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

# Creating an object of the Animal class
dog = Animal("Buddy", "Dog")
print(dog.name)  # Output: Buddy
print(dog.species)  # Output: Dog









class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Printing the instance to verify the attributes
print(my_car)  # Output: Toyota Corolla
