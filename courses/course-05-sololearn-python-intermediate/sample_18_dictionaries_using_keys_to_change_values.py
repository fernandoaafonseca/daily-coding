'''
You can use keys not only to access values in a dictionary, but also to change them.
'''


user = {
  'Name': 'Albert',
  'Age': 29
}

user['Age'] = 30

print(user['Age'])
print(user.items())