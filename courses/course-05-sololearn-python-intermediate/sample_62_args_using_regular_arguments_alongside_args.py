'''
When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.

For example:
'''


def show_items(category, *items):
  print(f'Category: {category}')

  for item in items:
    print(item)


show_items('Electronics', 'Laptop', 'Smartphone', 'Tablet')