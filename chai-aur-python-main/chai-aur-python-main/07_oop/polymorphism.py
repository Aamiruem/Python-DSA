# Polymorphism:
# The ability to use a unified interface to interact with objects of different types.




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
        return "meow!"

# Creating an object of the Dog class



class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.make_sound())

# Using the same interface for different types
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
