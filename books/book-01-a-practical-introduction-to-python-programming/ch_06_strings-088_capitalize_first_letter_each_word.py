'''
Write a program that asks the user to enter their name in lowercase and then capitalizes the first letter of each word of their name.
'''

def main() -> None:
	user_name = get_user_name()
	user_name_capitalized = user_name.title()
	display_result(user_name, user_name_capitalized)


def get_user_name() -> str:
	while True:
		try:
			user_name = str(input(f'Enter your name: '))
			return user_name
		except ValueError:
			print('\nPlease enter a valid string.\n')


def display_result(user_name: str, user_name_capitalized: str) -> None:
	print()
	print(f'You entered your name as follows: {user_name}.')
	print(f'Capitalizing your name: {user_name_capitalized}.')


if __name__ == '__main__':
	main()