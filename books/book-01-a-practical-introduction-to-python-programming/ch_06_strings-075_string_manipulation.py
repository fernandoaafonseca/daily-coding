'''
Write a program that asks the user to enter a string. The program should then print the following:
	(a) The total number of characters in the string
	(b) The string repeated 10 times
	(c) The first character of the string (remember that string indices start at 0)
	(d) The first three characters of the string
	(e) The last three characters of the string
	(f) The string backwards
	(g) The seventh character of the string if the string is long enough and a message otherwise
	(h) The string with its first and last characters removed
	(i) The string in all caps
	(j) The string with every a replaced with an e
	(k) The string with every letter replaced by a space
'''


def main():
	user_string = get_user_string()
	num_of_chars, str_repeated_10_times, first_char, first_3_chars, last_3_chars, backwards, seventh_char_output, str_with_first_and_last_chars_removed, all_caps, str_with_every_a_replaced_with_e, str_with_every_letter_replace_by_a_space = manipulate_user_string(user_string)
	display_result(user_string, num_of_chars, str_repeated_10_times, first_char, first_3_chars, last_3_chars, backwards, seventh_char_output, str_with_first_and_last_chars_removed, all_caps, str_with_every_a_replaced_with_e, str_with_every_letter_replace_by_a_space)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input('Enter a string (at least 3 characters long): '))
			if len(user_string) >= 3:
				return user_string
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid string with at least 3 characters.\n')


def manipulate_user_string(user_string: str) -> tuple[int, str, str, str, str, str, str, str, str, str, str]:
	num_of_chars = len(user_string)
	str_repeated_10_times = user_string * 10
	first_char = user_string[0]
	first_3_chars = user_string[0:3]
	last_3_chars = user_string[-3:]
	backwards = user_string[::-1]
	if num_of_chars >= 7:
		seventh_char_output = user_string[6]
	else:
		seventh_char_output = 'the string is less than 7 characters long'
	str_with_first_and_last_chars_removed = user_string[1:-1]
	all_caps = user_string.upper()
	str_with_every_a_replaced_with_e = user_string.replace('a', 'e')
	str_with_every_letter_replace_by_a_space = ''
	str_with_every_letter_replace_by_a_space = ' ' * num_of_chars

	return num_of_chars, str_repeated_10_times, first_char, first_3_chars, last_3_chars, backwards, seventh_char_output, str_with_first_and_last_chars_removed, all_caps, str_with_every_a_replaced_with_e, str_with_every_letter_replace_by_a_space


def display_result(user_string: str, num_of_chars: int, str_repeated_10_times: str, first_char: str, first_3_chars: str, last_3_chars: str, backwards: str, seventh_char_output: str, str_with_first_and_last_chars_removed: str, all_caps: str, str_with_every_a_replaced_with_e: str, str_with_every_letter_replace_by_a_space: str) -> None:
	print('=' * 20)
	print(f'Original input string: {user_string}')
	print('-' * 20)
	print(f'Number of characters in the string: {num_of_chars}')
	print('-' * 20)
	print(f'String repeated 10x: {str_repeated_10_times}')
	print('-' * 20)
	print(f'First character: {first_char}')
	print('-' * 20)
	print(f'First 3 characters: {first_3_chars}')
	print('-' * 20)
	print(f'Last 3 characters: {last_3_chars}')
	print('-' * 20)
	print(f'String backwards: {backwards}')
	print('-' * 20)
	print(f'Seventh character: {seventh_char_output}')
	print('-' * 20)
	print(f'String with its first and last characters removed: {str_with_first_and_last_chars_removed}')
	print('-' * 20)
	print(f'String in all caps: {all_caps}')
	print('-' * 20)
	print(f'String with every "a" replaced with an "e": {str_with_every_a_replaced_with_e}')
	print('-' * 20)
	print(f'String with every letter replaced by a space: {str_with_every_letter_replace_by_a_space}')
	print('=' * 20)


if __name__ == '__main__':
	main()