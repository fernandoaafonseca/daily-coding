'''
Recall that, given a string s, s.index('x') returns the index of the first x in s and an error if there is no x.

	(a) Write a program that asks the user for a string and a letter. Using a while loop, the program should print the index of the first occurrence of that letter and a message if the string does not contain the letter.
	(b) Write the above program using a for/break loop instead of a while loop.
'''


import os


def main() -> None:
	user_string = get_string()
	user_letter = get_letter()
	index_letter = find_index_first_occurence_of_letter(user_letter, user_string)
	display_result(user_string, user_letter, index_letter)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_string() -> str:
	while True:
		try:
			clear_terminal()

			user_string = str(input('Enter a string: '))

			all_chars_are_valid = all(char.isalpha() or char == ' ' for char in user_string)

			if len(user_string.replace(' ', '')) > 0 and all_chars_are_valid:
				return user_string
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a non-empty string using only letters.')
			press_any_key_to_continue()


def get_letter() -> str:
	while True:
		try:
			clear_terminal()

			user_letter = str(input('Enter a letter: '))

			all_chars_are_valid = all(char.isalpha() or char == ' ' for char in user_letter)

			if len(user_letter.replace(' ', '')) == 1 and all_chars_are_valid:
				return user_letter
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a single letter.')
			press_any_key_to_continue()


def find_index_first_occurence_of_letter(user_letter: str, user_string: str) -> int|str:
	index = 0

	while index < len(user_string):
		current_char = user_string[index].lower()
		if current_char == user_letter.lower():
			return index
		index += 1

	return f'The string does not contain the letter "{user_letter}".'


def display_result(user_string: str, user_letter: str, index_letter: int|str) -> None:
	clear_terminal()
	print(f'Your string: {user_string}')
	print(f'Letter to find: {user_letter}')

	if isinstance(index_letter, int):
		print(f'The first occurrence of the letter "{user_letter}" is at index {index_letter}.')
	else:
		print(index_letter)


if __name__ == '__main__':
	main()