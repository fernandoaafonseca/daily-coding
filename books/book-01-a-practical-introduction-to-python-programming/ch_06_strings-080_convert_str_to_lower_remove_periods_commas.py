'''
Write a program that asks the user to enter a string s and then converts s to lowercase, removes all the periods and commas from s, and prints the resulting string.
'''


def main():
	s = get_user_string()
	s = s.lower().replace('.', '').replace(',', '')
	display_result(s)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input('Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def display_result(user_string: str) -> None:
	print()
	print('Converting to lowercase and removing periods and commas...')
	print('RESULT:')
	print(user_string)


if __name__ == '__main__':
	main()