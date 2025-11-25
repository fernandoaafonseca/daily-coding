'''
The filter() function, just like the map() function, takes in a function and an iterable as arguments. The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable and return only those for which the function evaluates to True.

This code filters and returns products with names 4 characters long.
'''


products = ['Table', 'Sofa', 'Cushion', 'Bookshelf', 'Vase']

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)