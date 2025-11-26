'''
*args: tuple
**kwargs: dictionary

In a function definition, the order of arguments is important. First, regular arguments are listed, followed by *args for positional arguments, and finally **kwargs for keyword arguments.
'''


def show(class_name, *students, **info):
  print(f'Class: {class_name}')
  print('\nStudents:')

  for student in students:
    print(f'  - {student}')

  print('\nExtra info:')
  for key, value in info.items():
    print(f'  {key}: {value}')


show(
  # Regular argument
  'Python',
  # *args
  'Fernando', 'Alice', 'Bob',
  # **kwargs
  teacher='José',
  room='Lab 3',
  schedule='18:00'
)