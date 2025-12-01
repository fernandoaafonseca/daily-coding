'''
A good program will make sure that the data its users enter is valid. Write a program that asks the user for a weight and converts it from kilograms to pounds. Whenever the user enters a weight below 0, the program should tell them that their entry is invalid and then ask them again to enter a weight. [Hint: Use a while loop, not an if statement].
'''


import os


def main() -> None:
	kg = get_kg()
	pounds = convert_kg_to_pounds(kg)
	display_result(kg, pounds)


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def get_kg() -> float:
	while True:
		try:
			clear_terminal()
			kg = float(input('Enter a weight in kilograms: '))

			if kg > 0:
				return kg
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a valid weight in kilograms.')
			press_any_key_to_continue()


def convert_kg_to_pounds(kg: float) -> float:
	pounds = kg * 2.20462262185
	return round(pounds, 1)


def display_result(kg: float, pounds: float) -> None:
	print(f'{kg} kg = {pounds} lb')


if __name__ == '__main__':
	main()