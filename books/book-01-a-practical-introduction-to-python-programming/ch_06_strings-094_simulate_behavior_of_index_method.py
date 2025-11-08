'''
The goal of this exercise is to see if you can mimic the behavior of the "in" operator and the count and index methods using only variables, for loops, and if statements.

	(a) Without using the "in" operator, write a program that asks the user for a string and a letter and prints out whether or not the letter appears in the string.
	(b) Without using the count method, write a program that asks the user for a string and a letter and counts how many occurrences there are of the letter in the string.
	(c) Without using the index method, write a program that asks the user for a string and a letter and prints out the index of the first occurrence of the letter in the string. If the letter is not in the string, the program should say so.
'''


import string


def main() -> None:
	alphabet = string.ascii_lowercase
	user_string = get_user_string()
	user_letter = get_user_letter(alphabet)
	letter_index = get_letter_index_in_str(user_string, user_letter)
	display_result(user_string, user_letter, letter_index)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input(f'Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def get_user_letter(alphabet: str]) -> str:
	while True:
		try:
			user_letter = str(input(f'Enter the letter you want to find the index of: ')).lower()
			if len(user_letter) == 1 and user_letter in alphabet:
				return user_letter
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a single letter.\n')


def get_letter_index_in_str(user_string: str, user_letter: str) -> int | None:
	i = 0
	letter_index = None

	while i < len(user_string):
		if user_string[i] == user_letter:
			# The "index()" method returns the first instance of the value
			letter_index = i
			return letter_index
		i += 1

	return letter_index


def display_result(user_string: str, user_letter: str, letter_index: int|None) -> None:
	print()
	print(f'You entered the string: {user_string}.')

	if letter_index is not None:
		print(f'The first occurrence of the letter "{user_letter}" is at index {letter_index}.')
	else:
		print(f'The letter "{user_letter}" does not appear in the string.')


if __name__ == '__main__':
	main()