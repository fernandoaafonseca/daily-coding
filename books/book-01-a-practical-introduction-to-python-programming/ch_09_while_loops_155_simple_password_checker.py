'''
Write a program that asks the user to enter a password. If the user enters the right password, the program should tell them they are logged in to the system. Otherwise, the program should ask them to reenter the password. The user should only get five tries to enter the password, after which point the program should tell them that they are kicked off of the system.
'''


import os


PASSWORD = 'password'


def main() -> None:
	login()


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def login() -> None:
	attempts_left = 5
	while attempts_left > 0:
		user_password = get_password()
		attempts_left -= 1
		is_password_correct = check_password(user_password)

		if is_password_correct:
			print('\nLogged in succesfully')
			break

		elif attempts_left >= 1:
			print('\nInvalid password. Try again.')
			press_any_key_to_continue()

		else:
			print('\nYou are kicked off the system.')


def check_password(user_password: str) -> bool:
	return user_password == PASSWORD


def get_password() -> str:
	clear_terminal()
	user_password = str(input('Enter the password: '))
	return user_password


if __name__ == '__main__':
	main()