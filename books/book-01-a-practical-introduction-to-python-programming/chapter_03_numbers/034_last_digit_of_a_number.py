'''
(a) One way to find out the last digit of a number is to mod the number by 10. Write a program that asks the user to enter a power. Then find the last digit of 2 raised to that power.
'''


def main() -> None:
	exponent = get_exponent()
	result = calculate_power_of_two(exponent)
	last_digit = extract_last_digit(result)
	display_result(exponent, result, last_digit)


def get_exponent() -> int:
	while True:
		try:
			return int(input('Enter the power: '))
		except ValueError:
			print('Please enter an integer number.\n')


def calculate_power_of_two(exponent: int) -> int:
	return 2 ** exponent


def extract_last_digit(result: int) -> int:
	return result % 10


def display_result(exponent: int, result: int, last_digit: int) -> None:
	print(f'2^{exponent} = {result}')
	print(f'Last digit: {last_digit}')


if __name__ == '__main__':
	main()