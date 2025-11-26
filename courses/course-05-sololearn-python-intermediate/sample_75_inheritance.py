'''
The strength of OOP lies in organizing a program so its various components, treated as classes and objects, can interact smoothly.

In this lesson you will learn about the principle of inheritance, an OOP concept that enhances your program's versatility and efficiency.

Inheritance is a key concept for situations where you have an existing class with defined attributes and behaviors, and you need a new class that not only shares these characteristics but also has its own unique ones. Inheritance allows the new class to 'inherit' properties from the existing class while adding or modifying specific features as needed.

A class from which others are inherited is known as a superclass or parent class. Conversely, a class that inherits from another class is referred to as a subclass or child class.

The Dog class inherits from the Animal class.

When defining a child class, include the parent class name in parentheses.
'''


class Animal:
  def __init__(self, name):
    self.name = name

  def move(self):
    print('Moving')


# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print('Woof!')


# Creating an instance
my_dog = Dog('Bob')

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()