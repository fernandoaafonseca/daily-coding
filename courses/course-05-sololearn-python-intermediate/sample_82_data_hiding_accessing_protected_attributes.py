'''
Attributes with a single underscore are accessible but considered protected by convention, signaling they're for internal use and should be accessed cautiously outside the class.

To access a protected attribute outside of the class, use the single underscore prefix, as that's part of the attribute's name.
'''


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print(f'Odometer: {self._odometer} miles')


my_car = Car('Audi', 2020, 15000)

# Accessing the protected attribute
print(my_car._odometer)