'''
Functions can take other functions as arguments.

For example:
'''


def welcome(name):
  return f'Welcome, {name}'


def process_user(name, func):
    return func(name)


print(process_user('Alice', welcome))