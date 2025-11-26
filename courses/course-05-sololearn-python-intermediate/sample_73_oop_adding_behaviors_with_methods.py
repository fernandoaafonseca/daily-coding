'''
In addition to attributes, you can add custom behaviors to a class by defining functions within it. These functions, known as methods, should include the 'self' parameter to interact with the class instance. You can call these methods using the dot . notation, similar to how you access attributes.

The main difference between functions and methods is that functions are independent and can be called on their own, while methods are associated with a class and can be called only with its instance. This means that you can't call a method without having the instance of a class where that method is defined.
'''


class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

  def honk(self):
    print('Beep beep!')


my_car = Car('Audi', 'yellow')

my_car.honk()