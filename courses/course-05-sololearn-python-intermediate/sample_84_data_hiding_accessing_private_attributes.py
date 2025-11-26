'''
Accessing a private attribute directly from outside its class is generally discouraged in Python. However, Python employs name mangling for private attributes, which means you can access them using a specific naming convention from outside the class if necessary.

However, this approach should be used sparingly, as it bypasses the encapsulation principles intended by making the attribute private.

Here’s how you can do it:
'''


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print(f'Odometer: {self.__odometer} miles')


my_car = Car('Audi', 2020, 15000)

# Accesing using name mangling
print(my_car._Car__odometer)