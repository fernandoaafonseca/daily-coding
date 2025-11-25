'''
The update() function can accept dictionaries with multiple items.If an item is new, it will be added to the original dictionary.
'''


user = {
  'Name': 'Albert',
  'Age': 29
}

# 'Surname': 'Johnson' will be added
user.update({'Age': 30, 'Surname': 'Johnson'})

print(user.items())