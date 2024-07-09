# The concept of hiding complex implementation details and showing only the necessary features of an object.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an object of the Rectangle class
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30
