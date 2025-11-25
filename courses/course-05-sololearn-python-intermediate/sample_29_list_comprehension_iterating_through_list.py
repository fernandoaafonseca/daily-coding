'''
You can use a list as the iterable in a list comprehension.

For example, this code will iterate through the original list of tags, adding a '#' symbol to the beginning of each tag to create a new list of hashtags.
'''


tags = ['travel', 'vacation', 'journey']

hashtags = ['#' + x for x in tags]

print(hashtags)