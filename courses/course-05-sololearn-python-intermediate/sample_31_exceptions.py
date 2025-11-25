'''
Bugs, often caused by logical errors, can lead to unexpected or incorrect results. For example, the code below is meant to concatenate name and surname with a space. It executes without error but omits the space, which indicates a bug.
'''


name = 'Mery'
surname = 'Osborn'

print(name + surname)


'''
Exceptions are another category of mistakes in programming. These are specific errors that occur during a program's execution and interrupt its normal flow when first encountered.

For example, the program below will stop execution on the 2nd line:
'''


name = 'Bob'
name[0] = 'R'

print(name)