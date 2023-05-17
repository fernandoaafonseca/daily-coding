'''
Trying to think outside the box for this challenge, I discovered that Python has a module called "string" that contains characters separated by type, which made my life easier. So I turned everything into lists.

Then, I created a function that receives as arguments the amounts of each type of character that the user wants, I shuffled this list and returned it as a string.
'''

import random
import string

# make lists of the characters types using the "string" module
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

def generator (n_letters, n_numbers, n_symbols):
# function to add to a list all the characters with the arguments sent by the user
	
	password = []
	for char in range(1, n_letters+1):
		password.append(random.choice(letters))
		
	for num in range(1, n_numbers+1):
		password.append(random.choice(numbers))
		
	for symbol in range(1, n_symbols+1):
		password.append(random.choice(symbols))

# shuffle the characters in the password list
	random.shuffle(password)

# convert the password list into a string and return it
	password_string = ''.join(password)
	return password_string

print('Welcome to Pyssword Generator!\n')

n_letters = int(input('How many letters would you like?\n'))
n_numbers = int(input('How many numbers would you like?\n'))
n_symbols = int(input('How many symbols would you like?\n'))

# calls the function to generate the password, passing the user input arguments
password = generator(n_letters, n_numbers, n_symbols)

print(f'Your generated password is:\n{password}')