'''
Write a program that asks the user to enter a string, then prints out each letter of the string doubled and on a separate line. For instance, if the user entered HEY, the output would be

	HH
	EE
	YY
'''


def main() -> None:
	user_string = get_user_string()
	print_letters_doubled_on_new_lines(user_string)


def get_user_string() -> int:
	while True:
		try:
			user_string = str(input('Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def print_letters_doubled_on_new_lines(user_string: str) -> None:
	print()

	for i in range(len(user_string)):
		print(user_string[i] * 2)

if __name__ == '__main__':
	main()