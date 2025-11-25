'''
In Python, functions that operate with other functions — that is, take another function as an argument or return a function -  are called Higher-Order Functions. They are particularly useful for processing various functions and returning specific results.
'''


def welcome(name):
  return f'Welcome, {name}'


def bye(name):
  return f'Goodbye, {name}'


def process_user(name, func):
  return func(name)


print(process_user('Alice', welcome))
print(process_user('Bob', bye))