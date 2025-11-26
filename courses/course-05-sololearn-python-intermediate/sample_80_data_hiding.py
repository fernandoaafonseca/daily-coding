'''
Data hiding is a key idea in making code with objects (like in games or apps) safer and cleaner. It means keeping some parts of an object private so that only certain parts of your code can change them. This helps prevent mistakes and keeps your code easy to manage.

In this lesson, you'll explore how data hiding contributes to encapsulation in OOP, enhancing the security and robustness of your code.

Consider the Car class provided below. After creating an instance of this class, you can access and modify its attributes, as well as call its methods. Open the code, explore its functionality, and run it to observe the results.

In programming, sometimes it's crucial to 'protect' certain class attributes and methods from being accessed outside the class. This is called data hiding and ensures the integrity and security of the data, preventing unintended or harmful modifications.
'''


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print(f'Odometer: {self.odometer} miles')


my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

# Changing a value of the attribute
my_car.odometer = 20000

my_car.read_odometer()