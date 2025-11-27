'''
Write a program that asks the user to enter a length. The program should ask them what unit the length is in and what unit they would like to convert it to. The possible units are inches, yards, miles, millimeters, centimeters, meters, and kilometers. While this can be done with 25 if statements, it is shorter and easier to add on to if you use a two-dimensional list of conversions, so please use lists for this problem.
'''


import os


UNITS = ['in', 'yd', 'mi', 'mm', 'cm', 'm', 'km']
CONVERSIONS = [
	# in → [in,        	  yd,         	mi,             mm,         cm,        	m,          km]
			[1,        	  1/36,       	1/63360,        25.4,       2.54,      	0.0254,     0.0000254],

	# yd → [in,       	  yd,     		mi,            	mm,         cm,         m,          km]
			[36,       	  1,      		1/1760,        	914.4,		91.44,      0.9144,     0.0009144],

	# mi → [in,          yd,       		mi,     		mm,         cm,         m,         	km]
			[63360,		  1760,     	1,      		1_609_344,	160_934.4,	1609.344,	1.609344],

	# mm → [in,          yd,           mi,             mm,   		cm,   		m,      	km]
			[0.0393701,   0.00109361,   6.2137e-7,      1,    		0.1,  		0.001,  	0.000001],

	# cm → [in,          yd,          	mi,             mm,     	cm,  		m,     		km]
			[0.393701,    0.0109361,   	6.2137e-6,		10,     	1,   		0.01,  		0.00001],

	# m →  [in,          yd,       		mi,            	mm,     	cm,     	m,  		km]
			[39.3701,     1.09361,  	0.000621371,	1000,   	100,    	1,  		0.001],

	# km → [in,          yd,         	mi,         	mm,         cm,        	m,       	km]
			[39370.1,     1093.61,    	0.621371,   	1_000_000,  100_000,   	1000,    	1]
]


def main() -> None:
	original_length = get_length()
	original_unit = get_unit('Enter the unit the length is in: ')
	conversion_unit = get_unit('Enter the unit you want to convert to: ')
	converted_length = convert_length(original_length, original_unit, conversion_unit)

	display_result(original_length, original_unit, converted_length, conversion_unit)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_length() -> float:
	while True:
		try:
			clear_terminal()

			length = float(input('Enter a length: '))
			return length

		except ValueError:
			print('\nPlease enter a valid number.')
			press_any_key_to_continue()


def get_unit(prompt: str) -> str:
	while True:
		clear_terminal()
		print(prompt)
		print("Available units:", ', '.join(UNITS))

		unit = input('> ').lower().strip()
		if unit in UNITS:
			return unit

		print(f'\nPlease enter a valid unit.')
		press_any_key_to_continue()


def convert_length(original_length: float, original_unit: str, conversion_unit: str) -> float:
	original_unit_index = UNITS.index(original_unit)
	conversion_unit_index = UNITS.index(conversion_unit)

	return original_length * CONVERSIONS[original_unit_index][conversion_unit_index]


def display_result(original_length: float, original_unit: str, converted_length: float, conversion_unit: str) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'{original_length:.2f}{original_unit} ≈ {converted_length:.2f}{conversion_unit}')


if __name__ == '__main__':
	main()