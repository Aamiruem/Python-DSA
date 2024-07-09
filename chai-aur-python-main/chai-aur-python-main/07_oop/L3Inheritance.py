# Define the ElectricCar class and make it inherit from the Car class.
# Add the battery_size attribute to the ElectricCar class.
# Override the constructor (__init__) method to initialize the battery_size attribute along with the inherited attributes brand and model.
# Optionally, you can add methods specific to ElectricCar if needed.




class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def display_full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Initialize brand and model from the parent class
        self.battery_size = battery_size  # Initialize battery_size specific to ElectricCar

    def display_full_name(self):
        return f"{self.brand} {self.model} with a {self.battery_size}-kWh battery"

# Creating an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Using the display_full_name method
print(my_electric_car.display_full_name())  # Output: Tesla Model S with a 100-kWh battery











# Class Definition:

# class Car: Defines the base Car class with brand and model attributes.
# def __init__(self, brand, model): Initializes the brand and model attributes.
# def __str__(self): Provides a string representation of the car.
# def display_full_name(self): Returns the full name of the car.
# Inheritance:

# class ElectricCar(Car): Defines the ElectricCar class that inherits from the Car class.
# Constructor Override:

# def __init__(self, brand, model, battery_size): Overrides the constructor to include the battery_size attribute.
# super().__init__(brand, model): Calls the constructor of the parent Car class to initialize the brand and model attributes.
# self.battery_size = battery_size: Initializes the battery_size attribute specific to the ElectricCar.
# Method Override:

# def display_full_name(self): Overrides the display_full_name method to include the battery_size in the output.
# Instance Creation and Method Call:

# my_electric_car = ElectricCar("Tesla", "Model S", 100): Creates a new instance of the ElectricCar class with brand set to "Tesla", model set to "Model S", and battery_size set to 100.
# print(my_electric_car.display_full_name()): Calls the display_full_name method on the my_electric_car object and prints the returned value, which includes the battery size.
