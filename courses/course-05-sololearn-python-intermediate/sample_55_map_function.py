'''
The power of lambda expressions becomes evident when working with data manipulation and transformation tasks.

In this lesson, you will learn how to effectively use lambda expressions with functions that are specifically designed for processing and transforming iterables.

The map() function applies a specified function to every element in an iterable, like lists or tuples. It produces a result that can be transformed into a list using the list() function for easy viewing or further use.
'''


# List of names in various cases
names = ['alice', 'bob', 'CHARLIE', 'dEborah']

# Function to capitalize each name
def capitalize(name):
  return name.capitalize()


# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)