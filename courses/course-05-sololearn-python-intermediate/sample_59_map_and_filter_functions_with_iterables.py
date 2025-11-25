'''
The map() and filter() functions can work with any iterable. In the example below, filter() is used to extract items from the products dictionary, where prices are under 90.
'''


products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}

# Filtering products with prices less than 90
filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))

print(filtered_products)