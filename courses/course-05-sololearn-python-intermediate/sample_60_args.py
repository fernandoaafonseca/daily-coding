'''
Up to this point, you've been defining functions with a fixed number of known arguments.

In this section, you will learn about techniques that enhance the adaptability of functions, making them more versatile and ready for different scenarios.

If the number of arguments of your function is unknown and unpredictable, you can always use an iterable as an argument.

*args allows you to provide any number of arguments without the need to create a list before calling the function each time.

For example:
'''


def total(*args):
  result = 0

  for arg in args:
    result += arg

  return result


print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))