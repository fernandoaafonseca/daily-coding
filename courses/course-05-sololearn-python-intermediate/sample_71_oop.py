'''
You've made fantastic progress and have mastered many fundamental Python concepts, including variables, data types, loops, iterables, and functions. Now, it's time to delve into another essential programming paradigm: object-oriented programming (OOP).

In this lesson, you will learn about classes and objects and learn how they are created in Python.

In the real world, most things have a 'blueprint' and multiple instances of it. By 'blueprint,' we refer to an abstract set of properties and behaviors. Take, for example, a 'car.' It's a blueprint, or a general idea, covering properties like having four wheels, a color, engine power, and so on. The cars you see on the road are specific instances of this general blueprint, each with its unique characteristics like color, make, and model.

In programming, there is a paradigm that follows the same principle as blueprints and instances. It's called object-oriented programming (OOP). In OOP, blueprints are referred to as classes, and the instances are known as objects.

In the real world, everything has distinguishing characteristics: a dog has its breed, color, and name; a car has its brand, model, and color. In programming, classes and objects mirror this concept with attributes. Attributes are the properties that define an object's individuality within a class.

To add attributes to a class, you must define the __init__ method. This method's first parameter is always self, which represents the instance of the class. Following self, you specify the attributes you wish to include. Then, inside the function, you assign values to the initialized object's attributes, setting their initial state.

In Python, you can define a class by using the class keyword followed by the class name and a colon.
'''


class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color


# Create an object of the Car class
my_car = Car('Audi', 'yellow')

print(my_car)