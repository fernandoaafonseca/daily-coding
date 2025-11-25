'''
The update() function updates the dictionary with the items from the given argument.

The argument must be a dictionary with the item you want to update.
'''


user = {
  'Name': 'Albert',
  'Age': 29
}

# Argument: dictionary {'Age': 30}
user.update({'Age': 30})

print(user['Age'])
print(user.items())