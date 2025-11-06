'''
Write a program that asks the user to enter a string. The program should create a new string called new_string from the user’s string such that the second character is changed to an asterisk and three exclamation points are attached to the end of the string. Finally, print new_string. Typical output is shown below:

Enter your string: Qbert
Q*ert!!!
'''


def main():
	user_string = get_user_string()
	new_string = change_user_string(user_string)
	display_result(user_string, new_string)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input('Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def change_user_string(user_string: str) -> str:
	'''
	user_string[:1] → takes the first character (index 0);
	'*' → replaces the second character (index 1);
	user_string[2:] → takes from the third character onward;
	'!!!' → adds three exclamation marks at the end.
	'''
	return user_string[:1] + '*' + user_string[2:] + '!!!'


def display_result(user_string: str, new_string: str) -> None:
	print()
	print(f'Your original string: "{user_string}"')
	print(f'Modified string: "{new_string}"')


if __name__ == '__main__':
	main()