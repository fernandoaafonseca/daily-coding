'''
Do you remember lambda expressions? Another valuable aspect of them is their ability to be directly provided to the map function. This eliminates the need to define a regular function explicitly.
'''


numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)