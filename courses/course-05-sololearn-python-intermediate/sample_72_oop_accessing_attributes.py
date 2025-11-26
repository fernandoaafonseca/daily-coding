'''
After an object is created, you can access its attributes by using the dot . notation with the variable holding the object.
'''


class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color


# Create an object of the Car class
my_car = Car('Audi', 'yellow')


# Display attribute values
print(my_car.brand)
print(my_car.color)