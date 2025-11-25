'''
The pop() function removes the item with the specified key name. It accepts the key of the item you want to remove as an argument.
'''


car = {
  'Brand': 'Ford',
  'Model': 'Mustang',
  'Color': 'red'
}

# Removing the item with the 'Color' key
car.pop('Color')
print(car)