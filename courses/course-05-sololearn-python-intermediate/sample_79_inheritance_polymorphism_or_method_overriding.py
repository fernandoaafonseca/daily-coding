'''
Method overriding is a demonstration of another key concept in OOP - polymorphism. Polymorphism lets objects use methods in their own way, even if they share the same name.

In this example, even though each animal in the animals list may be of a different subclass, the code can call sound() on each without needing to know its specific type.
'''


# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print('Making a sound')


# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Dog
  def sound(self):
    print('Woof!')


# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print('Meow!')


# Creating instances
my_dog = Dog('Jax', 'Bulldog', 5)
my_cat = Cat('Lily', 'Ragdoll', 2)

animals = [my_dog, my_cat]

for animal in animals:
  animal.sound()