# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Here, we're defining a new "class" called "Car."
# Think of it as a blueprint for making cars.
# Class Definition
class Car:
    # This is a special function that gets called when a new car is created.
    # It's like the instructions for what to do when making a new car.
    # Constructor (Initialization) - __init__ method
    def __init__(self, make, model):
        # "self" refers to the car that's being created.
        # We're storing the "make" and "model" information in the car.

        # Encapsulation: Attributes (make and model) are encapsulated within the class.
        # Encapsulation hides the internal details of an object and exposes only what is necessary.
        # Think of it as specifying the unique characteristics of each car.
        self.make = make
        self.model = model

    # This is a method, which is like a function inside the class.
    # It's something the car can do, like starting its engine.
    # Method - start_engine
    def start_engine(self):
        # Encapsulation: Accessing attributes through self.
        # Analogously, this is like the car performing an action specific to itself.
        print(f"The {self.make} {self.model}'s engine is running!")

# Creating instances (objects) of the Car class

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.
# Think of creating individual cars without needing to understand the intricacies of car manufacturing.

# Creating the first car (object)
car1 = Car("Toyota", "Camry")

# Creating the second car (object)
car2 = Car("Ford", "Mustang")

# Accessing object attributes

# Encapsulation: Accessing object attributes (make and model) using dot notation.
# It's like checking the make and model of each car without knowing how they are implemented internally.
print(f"I have a {car1.make} {car1.model}.")
print(f"I also own a {car2.make} {car2.model}.")

# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).
# Method Overriding: The start_engine method may be customized in subclasses.
# This is like both cars can starting their engines, but each might do it in a way specific to its make and model.

# Method Call - start_engine
car1.start_engine()  # Polymorphism: Car 1 starts its engine.
car2.start_engine()  # Polymorphism: Car 2 starts its engine.
# This is like instructing each car to engage its engine, and they follow their unique set of instructions.