'''
Write a Python program to check whether the given string is a palindrome or not.
'''


def main() -> None:
	user_string = get_string()
	cleaned_user_string = remove_non_alphanumeric_chars(user_string)
	reversed_user_string = reverse_string(cleaned_user_string)
	is_palindrome = check_palindrome(cleaned_user_string, reversed_user_string)

	display_result(user_string, cleaned_user_string, reversed_user_string, is_palindrome)


def get_string() -> str:
	while True:
		try:
			user_string = str(input('Enter a word or phrase: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid word or phrase.\n')


def remove_non_alphanumeric_chars(user_string: str) -> str:
    '''
    Removes non-alphanumeric characters from a string using a list comprehension.
    '''
    return ''.join(char for char in user_string if char.isalnum())


def reverse_string(cleaned_user_string: str) -> str:
	string_length = len(cleaned_user_string)

	reversed_user_string = ''
	for i in range(string_length - 1, -1, -1):
		reversed_user_string += cleaned_user_string[i]

	return reversed_user_string


def check_palindrome(cleaned_user_string: str, reversed_user_string: str) -> bool:
	return cleaned_user_string == reversed_user_string


def display_result(user_string: str, cleaned_user_string: str, reversed_user_string: str, is_palindrome: bool) -> None:
	print(f'\nOriginal input string: {user_string}')
	print(f'After removing non-alphanumeric characters: {cleaned_user_string}')
	print(f'Reversed string: {reversed_user_string}\n')

	if is_palindrome:
		print(f'✔️ Yes! "{user_string}" is a palindrome!')
		print(f'"{cleaned_user_string}" = "{reversed_user_string}"')
	else:
		print(f'❌ No! "{user_string}" is not a palindrome.')
		print(f'"{cleaned_user_string}" ≠ "{reversed_user_string}"')


if __name__ == '__main__':
	main()