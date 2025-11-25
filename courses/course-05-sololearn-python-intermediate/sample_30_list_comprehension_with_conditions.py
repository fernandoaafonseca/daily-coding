'''
You can incorporate a condition into a list comprehension, placed after the iterable.

For example, the following code filters out names that start with B.
'''


users = ['Brandon', 'Emma', 'Brian',
'Sophia', 'Bella', 'Ethan',
'Ava', 'Benjamin', 'Mia', 'Chloe']

group = [x for x in users if x[0] == 'B']

print(group)