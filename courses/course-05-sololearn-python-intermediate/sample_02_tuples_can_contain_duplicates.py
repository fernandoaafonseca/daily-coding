'''
Tuples, like lists, can contain duplicate elements.

You can use the count() function to calculate the number of occurrences of an item in a tuple.
'''


scores = (7, 9, 9, 8, 9)

print(f'# of 7: {scores.count(7)}')
print(f'# of 79: {scores.count(9)}')
print(f'# of 2: {scores.count(2)}')