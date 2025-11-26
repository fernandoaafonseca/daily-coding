'''
The first line of the function definition, which includes the function name and its parameters, is called function signature.

Python also allows you to pass keyword arguments using **kwargs. In this case, **kwargs receives arguments in the form of a dictionary, consisting of key:value pairs.

The ** operator in Python is used to unpack dictionaries into arguments. It enables a function to accept an arbitrary number of keyword arguments, converting these arguments into a dictionary of key:value pairs.
'''


# **kwargs is a dictionary
def display_info(**kwargs):
  # kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(f'{key}: {value}')


display_info(name="Alice", age=30, city="New York")