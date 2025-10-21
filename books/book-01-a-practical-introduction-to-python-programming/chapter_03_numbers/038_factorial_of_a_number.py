'''
Write a program that asks the user for a number and prints out the factorial of that number.
'''


def main() -> None:
	num = get_user_num()
	factorial = calculate_factorial(num)
	display_result(num, factorial)


def get_user_num() -> int:
	while True:
		try:
			num = int(input('Enter a positive integer number: '))
			if num >= 0:
				return num
			else:
				raise ValueError()
		except ValueError:
			print('Please enter a integer number.\n')


def calculate_factorial(num: int) -> int:
	if num > 0:
		factorial = 0

		for i in range(num - 1, 1, -1):
			factorial *= i

	else:
		factorial = 1

	return factorial


def display_result(num: int, factorial: int) -> None:
	print(f'{num}! = {factorial}')


if __name__ == '__main__':
	main()
