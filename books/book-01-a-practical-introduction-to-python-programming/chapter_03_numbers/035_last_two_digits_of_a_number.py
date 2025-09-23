'''
(b) One way to find out the last two digits of a number is to mod the number by 100. Write a program that asks the user to enter a power. Then find the last two digits of 2 raised to that power.
'''


def main() -> None:
	exponent = get_exponent()
	result = calculate_power_of_two(exponent)
	last_two_digits = extract_last_two_digits(result)
	display_result(exponent, result, last_two_digits)


def get_exponent() -> int:
	while True:
		try:
			return int(input('Enter the power: '))
		except ValueError:
			print('Please enter an integer number.\n')


def calculate_power_of_two(exponent: int) -> int:
	return 2 ** exponent


def extract_last_two_digits(result: int) -> int:
	return result % 100


def display_result(exponent: int, result: int, last_two_digits: int) -> None:
	print(f'2^{exponent} = {result}')
	print(f'Last two digits: {last_two_digits}')


if __name__ == '__main__':
	main()