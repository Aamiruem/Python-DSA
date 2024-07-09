Class Definition:

# class Car: Defines the Car class.
# def __init__(self, brand, model): The constructor initializes the __brand (private attribute) and model attributes.
# self.__brand = brand: Sets the __brand attribute to the value passed during instantiation. The double underscore prefix makes it a private attribute.
# def __str__(self): Provides a string representation of the car.
# def display_full_name(self): Returns the full name of the car using the private __brand attribute.
# Encapsulation:

# The __brand attribute is private, meaning it cannot be accessed directly from outside the class.
# Getter Method:

# def get_brand(self): A getter method that returns the value of the private __brand attribute.
# Instance Creation and Method Call:

# my_car = Car("Toyota", "Corolla"): Creates an instance of the Car class with brand set to "Toyota" and model set to "Corolla".
# print(my_car.get_brand()): Calls the get_brand method to access the private __brand attribute and prints the returned value.
# print(my_car.display_full_name()): Calls the display_full_name method to print the full name of the car.
