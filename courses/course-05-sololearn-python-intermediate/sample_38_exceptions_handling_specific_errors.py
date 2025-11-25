'''
To handle a specific type of exception, you need to specify it in the except block.
'''


color = 'Green'

try:
  print(colour)
except NameError:
  print("Check the variable name")