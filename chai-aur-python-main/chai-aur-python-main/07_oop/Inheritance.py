# Inheritance:
# A mechanism where a new class inherits properties and methods from an existing class.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def full_name(self):
        return f"{self.name} the {self.species}"




class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Creating an object of the Dog class
buddy = Dog("Buddy", "Dog")
print(buddy.make_sound())  # Output: Woof!
