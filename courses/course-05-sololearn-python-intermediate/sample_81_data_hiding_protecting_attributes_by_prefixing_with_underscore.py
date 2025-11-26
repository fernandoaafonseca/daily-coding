'''
In Python, data hiding has two levels. The first involves prefixing an attribute with a single underscore _, signaling it's meant for internal use and should be viewed as 'protected'.

Let's make this change with the odometer attribute:
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

my_car.describe_car()
my_car.read_odometer()