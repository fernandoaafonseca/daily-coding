'''
(c) Write a program that asks the user to enter a power and how many digits they want. Find the last that many digits of 2 raised to the power the user entered.
'''


def main() -> None:
	exponent = get_exponent()
	amount_of_last_digits = get_amount_of_last_digits()
	result = calculate_power_of_two(exponent)
	last_digits = extract_last_digits(amount_of_last_digits, result)
	display_result(exponent, amount_of_last_digits, result, last_digits)


def get_exponent() -> int:
	while True:
		try:
			return int(input('Enter the power: '))
		except ValueError:
			print('Please enter an integer number.\n')


def get_amount_of_last_digits() -> int:
	while True:
		try:
			return int(input('Enter the amount of last digits you want: '))
		except ValueError:
			print('Please enter an integer number.\n')


def calculate_power_of_two(exponent: int) -> int:
	return 2 ** exponent


def extract_last_digits(amount_of_last_digits: int, result: int) -> int:
	return result % (10 ** amount_of_last_digits)


def display_result(exponent: int, amount_of_last_digits: int, result: int, last_digits: int) -> None:
	print(f'2^{exponent} = {result}')
	print(f'Last {amount_of_last_digits} digits: {last_digits}')


if __name__ == '__main__':
	main()