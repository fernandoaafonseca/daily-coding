'''
Dictionaries can have duplicate values, but not duplicate keys.

Values with duplicate keys will overwrite existing values.
'''


car = {
  'brand': 'Audi',
  'model': 'Q5',
  'model': 'A5'
}

print(car)