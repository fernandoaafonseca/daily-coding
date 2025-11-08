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
	letter_count = count_letter_occurrences_in_str(user_string, user_letter)
	display_result(user_string, user_letter, letter_count)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input(f'Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def get_user_letter(alphabet: str) -> str:
	while True:
		try:
			user_letter = str(input(f'Enter the letter you want to count: ')).lower()
			if len(user_letter) == 1 and user_letter in alphabet:
				return user_letter
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a single letter.\n')


def count_letter_occurrences_in_str(user_string: str, user_letter: str) -> int:
	i = 0
	counter = 0

	while i < len(user_string):
		if user_string[i] == user_letter:
			counter += 1
		i += 1

	return counter


def display_result(user_string: str, user_letter: str, letter_count: int) -> None:
	if letter_count == 1:
		time_or_times = 'time'
	else:
		time_or_times = 'times'

	print()
	print(f'You entered the string: {user_string}.')
	print(f'The letter "{user_letter}" appears {letter_count} times in the string.')


if __name__ == '__main__':
	main()