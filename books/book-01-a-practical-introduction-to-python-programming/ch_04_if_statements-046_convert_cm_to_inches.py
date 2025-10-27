'''
Write a program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. There are 2.54 centimeters in an inch.
'''


def main():
	length_in_cm = get_length_in_cm()
	length_in_inches = convert_cm_to_inches(length_in_cm)
	display_result(length_in_cm, length_in_inches)


def get_length_in_cm() -> float:
	while True:
		try:
			length_in_cm = float(input('Enter a length in centimeters: '))
			if length_in_cm > 0:
				return length_in_cm
			else:
				raise ValueError
		except ValueError:
			print('Please enter a positive number.\n')


def convert_cm_to_inches(length_in_cm: float) -> float:
	return length_in_cm / 2.54


def display_result(length_in_cm: float, length_in_inches: float) -> None:
	print(f'{length_in_cm} cm ≈ {length_in_inches:.2f} inches')


if __name__ == '__main__':
	main()
