'''
You can have multiple except blocks to handle each possible exception specifically. As a best practice, it is recommended to output a definitive message for each type of handled exception.
'''


colors = ['Red', 'Yellow', 'Green']

try:
  print(colors[10])
except IndexError:
  print('Out of range')
except NameError:
  print('Variable is not defined')

print('Happy shopping')