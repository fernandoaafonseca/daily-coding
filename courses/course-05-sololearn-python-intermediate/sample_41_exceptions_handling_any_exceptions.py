'''
You can choose not to specify the exception type, which allows handling of any exceptions that may occur. While this approach is easier, the downside is that the error messages may not be as clear and helpful.
'''


colors = ['Red', 'Yellow', 'Green']

try:
  print(colors[10])
except:
  print('Error')