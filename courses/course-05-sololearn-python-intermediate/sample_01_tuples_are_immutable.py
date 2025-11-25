'''
So, what's the difference between tuples and lists? Tuples are immutable.

They are useful when the data stored in collections shouldn't be accidentally modified during the program execution. For example, in a GPS navigation application, the coordinates of landmarks should remain constant.
'''


eiffel_tower = (48.8584, 2.2945)
eiffel_tower[0] = 56.7581 # error