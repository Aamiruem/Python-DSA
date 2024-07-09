# Define the fuel_type method in the Car class to return the type of fuel a traditional car uses.
# Define the fuel_type method in the ElectricCar class to return the type of fuel an electric car uses.
# Create instances of both classes and call the fuel_type method to see polymorphism in action.






class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    def __str__(self):
        return f"{self.__brand} {self.model}"

    def display_full_name(self):
        return f"{self.__brand} {self.model}"

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Method to demonstrate polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Initialize brand and model from the parent class
        self.battery_size = battery_size  # Initialize battery_size specific to ElectricCar

    def display_full_name(self):
        return f"{self.get_brand()} {self.model} with a {self.battery_size}-kWh battery"

    # Overriding the fuel_type method to demonstrate polymorphism
    def fuel_type(self):
        return "Electricity"

# Creating instances of Car and ElectricCar
my_car = Car("Toyota", "Corolla")
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Using the fuel_type method
print(my_car.display_full_name())  # Output: Toyota Corolla
print(my_car.fuel_type())  # Output: Petrol or Diesel

print(my_electric_car.display_full_name())  # Output: Tesla Model S with a 100-kWh battery
print(my_electric_car.fuel_type())  # Output: Electricity







# Class Definition:

# class Car: Defines the base Car class with private attribute __brand, public attribute model, and methods display_full_name, get_brand, and fuel_type.
# def fuel_type(self): Defines a method that returns the type of fuel a traditional car uses ("Petrol or Diesel").
# Inheritance:

# class ElectricCar(Car): Defines the ElectricCar class that inherits from the Car class.
# Constructor Override:

# def __init__(self, brand, model, battery_size): Initializes the ElectricCar with brand, model, and battery_size.
# Method Override:

# def fuel_type(self): Overrides the fuel_type method in the ElectricCar class to return "Electricity".
# Polymorphism:

# my_car = Car("Toyota", "Corolla"): Creates an instance of the Car class.
# my_electric_car = ElectricCar("Tesla", "Model S", 100): Creates an instance of the ElectricCar class.
# print(my_car.fuel_type()): Calls the fuel_type method on a Car object, outputting "Petrol or Diesel".
# print(my_electric_car.fuel_type()): Calls the fuel_type method on an ElectricCar object, outputting "Electricity".
