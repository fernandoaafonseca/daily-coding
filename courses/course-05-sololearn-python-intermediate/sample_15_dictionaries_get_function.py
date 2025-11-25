'''
Another way to access values in a dictionary is through the get() function.

It's called on a dictionary using dot . notation and accepts the key as an argument
'''


car = {
  'brand': 'Audi',
  'model': 'Q5',
  'year': '2008'
}

print(car.get('brand'))
print(car.get('model'))
print(car.get('year'))