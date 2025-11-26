'''
The next level of data hiding involves making an attribute private. This is achieved by prefixing the attribute name with two underscores (e.g., __attribute). In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation. This method is used for sensitive or internal data, strongly discouraging external access.

Accessing a private attribute with double underscores from outside the class causes an error, but it's accessible within class methods. This demonstrates encapsulation, protecting sensitive data from external access and ensuring it's only reachable via specific methods, aligning with object-oriented programming principles.
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

# Accessing the attribute within method
my_car.read_odometer()

# Error
print(my_car.__odometer)