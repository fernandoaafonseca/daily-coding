'''
When you specify only one type of exception to be handled, other types of exceptions will not be covered. If these other exceptions occur, the program execution will fail.

For instance, the execution of this code will fail because the exception it throws is not handled.
'''


colors = ['Red', 'Yellow', 'Green']

try:
  # Index error
  print(colors[10])

  # Wrong exception
except NameError:
  print('Error')

# Will not be executed
print('Happy Shopping')