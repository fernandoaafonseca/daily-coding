'''
The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.
'''


books = ['Harry Potter', 'Dune', 'Emma']

try:
  choice = books[1]
except IndexError:
  print('Out of range')
else:
  print(f'{choice} is a great choice!')