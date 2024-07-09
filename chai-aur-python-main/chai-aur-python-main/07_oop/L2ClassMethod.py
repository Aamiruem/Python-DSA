# To add a method to the Car class that displays the full name of the car (brand and model), you can define a new method within the class. This method will use the self parameter to access the instance attributes brand and model.






class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def display_full_name(self):
        return f"{self.brand} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Using the display_full_name method
print(my_car.display_full_name())  # Output: Toyota Corolla








# Class Definition:

# class Car: Defines a new class named Car.
# def __init__(self, brand, model): The constructor method that initializes the brand and model attributes when a new Car object is created.
# self.brand = brand: Sets the brand attribute of the object to the value passed during instantiation.
# self.model = model: Sets the model attribute of the object to the value passed during instantiation.
# def __str__(self): Defines a method to return a string representation of the Car object, which makes it easier to understand the object's state when printed.
# def display_full_name(self): Defines a method to return the full name of the car, which is a combination of the brand and model attributes.
# Instance Creation and Method Call:

# my_car = Car("Toyota", "Corolla"): Creates a new instance of the Car class with brand set to "Toyota" and model set to "Corolla".
# print(my_car.display_full_name()): Calls the display_full_name method on the my_car object and prints the returned value, which is the full name of the car.
