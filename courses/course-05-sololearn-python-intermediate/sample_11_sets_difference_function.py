'''
The difference() function returns a set containing elements that are only in the first set and not in the second.
'''


set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}

unique = set1.difference(set2)

print(unique)