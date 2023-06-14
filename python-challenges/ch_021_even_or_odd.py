'''
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''


def even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'


print(even_or_odd(4) == 'even')
print(even_or_odd(7) == 'odd')
