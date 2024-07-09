# Define the Car Class:

# Create the __init__ method to initialize the brand and model attributes.
# Optionally, you can add a __str__ method to provide a string representation of the Car object.
# Create an Instance of the Car Class:

# Instantiate the Car class with specific brand and model values.
# Print the instance to verify that it has been created correctly.



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






# Class Definition:

# class Car: Defines a new class named Car.
# def __init__(self, brand, model): The constructor method that initializes the brand and model attributes when a new Car object is created.
# self.brand = brand: Sets the brand attribute of the object to the value passed during instantiation.
# self.model = model: Sets the model attribute of the object to the value passed during instantiation.
# def __str__(self): Defines a method to return a string representation of the Car object, which makes it easier to understand the object's state when printed.
# Instance Creation:

# my_car = Car("Toyota", "Corolla"): Creates a new instance of the Car class with brand set to "Toyota" and model set to "Corolla".
# print(my_car): Prints the string representation of the my_car object, which is defined in the __str__ method of the Car class.
