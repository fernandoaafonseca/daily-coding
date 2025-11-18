'''
Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards, etc. While this can be done with if statements, it is much shorter with lists and it is also easier to add new conversions if you use lists.
'''


import os


def main():
	feet = get_length_in_feet()
	choice = get_conversion_choice()
	converted_unit, converted_value = convert_length(feet, choice)
	display_result(feet, converted_unit, converted_value)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_length_in_feet() -> float:
	while True:
		press_any_key_to_continue()
		clear_terminal()

		try:
			feet = float(input('Enter a length in feet: '))
			return feet
		except ValueError:
			print('\nPlease enter a valid length in feet.')


def get_conversion_choice() -> int:
	while True:
		press_any_key_to_continue()
		clear_terminal()

		try:
			print('Convert to:')
			print('1 - Inches')
			print('2 - Yards')
			print('3 - Miles')
			print('4 - Millimeters')
			print('5 - Centimeters')
			print('6 - Meters')
			print('7 - Kilometers')

			choice = int(input('\nEnter your choice (1-7): '))
			if 1 <= choice <= 7:
				return choice
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a number between 1 and 7.')


def convert_length(feet: float, choice: int) -> tuple[str, float]:
	'''
	Choice values:
		1 - Inches
		2 - Yards
		3 - Miles
		4 - Millimeters
		5 - Centimeters
		6 - Meters
		7 - Kilometers
	'''
	UNITS = ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']
	UNITS_FACTORS = [
	12.0,					# feet → inches
	0.3333333333333333,		# feet → yards
	0.0001893939393939,		# feet → miles
	304.8,					# feet → millimeters
	30.48,					# feet → centimeters
	0.3048,					# feet → meters
	0.0003048				# feet → kilometers
	]

	converted_unit = UNITS[choice - 1]
	converted_value = feet * UNITS_FACTORS[choice - 1]

	return converted_unit, converted_value


def display_result(feet: float, converted_unit: str, converted_value: float) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'Converting feet to {converted_unit}...')
	print(f'{feet} feet ≈ {converted_value:.4f} {converted_unit}')


if __name__ == '__main__':
	main()