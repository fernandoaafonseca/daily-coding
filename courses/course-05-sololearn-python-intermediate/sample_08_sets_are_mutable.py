'''
Sets are mutable, meaning you can add or remove items from them.

Use the add() and remove() functions, each with a value as an argument, to add or remove it from a set.
'''


guests = {'Anna', 'Mery', 'Jonathan'}

# Adding 'Robert'
guests.add('Robert')

# Removing 'Mery'
guests.remove('Mery')

print(guests)