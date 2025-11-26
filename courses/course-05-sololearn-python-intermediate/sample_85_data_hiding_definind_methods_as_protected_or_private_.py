'''
You can also designate methods as protected or private, following the same convention as with attributes. Protected methods are prefixed with a single underscore and can be accessed within the class and its subclasses. However, private methods, marked by a double underscore, cannot be directly accessed from outside the class.


'''


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer

  def _describe_car(self):
  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):
  # Making the read_odometer method 'private'
    print(f'Odometer: {self.__odometer} miles')


my_car = Car('Audi', 2020, 15000)

# Accessing protected method
my_car._describe_car()

# Error when accessing a privet method
my_car.__read_odometer()