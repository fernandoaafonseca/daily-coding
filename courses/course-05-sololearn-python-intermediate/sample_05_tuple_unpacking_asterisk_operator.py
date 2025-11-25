'''
The * operator in tuple unpacking is used to gather multiple elements from the tuple into a list. This is useful when dealing with tuples of unknown length.
'''


scores = (98, 96, 91, 88, 64)
winner, *rest = scores

print(winner)
print(rest)