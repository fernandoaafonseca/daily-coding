'''
Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed.
'''


def main():
	user_list = get_list_of_str()
	user_list_without_first_chars = remove_first_chars(user_list)
	display_result(user_list, user_list_without_first_chars)


def get_list_of_str() -> list[str]:
	while True:
		try:
			user_str = str(input('Enter a list of strings separated by commas: '))
			# Generates a list of "strings" splitting the string by "commas" and removing the leading empty spaces before each string with "lstrip()"
			user_list = [str(item.lstrip()) for item in user_str.split(',')]

			return user_list
		except ValueError:
			print('\nPlease enter a valid list of strings separated by commas.\n')


def remove_first_chars(user_list: list[str]) -> list[str]:
	return [item[1:] for item in user_list]


def display_result(user_list: list[str], user_list_without_first_chars: list[str]) -> None:
	print()
	print(f'Original list: \n{user_list}')
	print(f'\nRemoving first characters: \n{user_list_without_first_chars}')


if __name__ == '__main__':
	main()