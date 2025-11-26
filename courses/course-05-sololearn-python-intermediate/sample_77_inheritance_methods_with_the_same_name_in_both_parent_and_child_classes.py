'''
You can define methods with the same name in both parent and child classes, but they can perform different operations. This is known as method overriding. For instance, consider the Animal class with a sound method. The Dog and Cat child classes inherit the sound method from Animal but override it to suit their specific needs.
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
    print("Meow!")


# Creating instances
my_dog = Dog('Jax', 'Bulldog', 5)
my_cat = Cat('Lily', 'Ragdoll', 2)

# Using overridden methods
my_dog.sound()
my_cat.sound()