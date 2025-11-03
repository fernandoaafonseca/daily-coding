'''
Write a program that computes the factorial of a number. The factorial, n!, of a number n is the product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120. [Hint: Try using a multiplicative equivalent of the summing technique.]
'''


def main() -> None:
	num = get_user_num()
	factorial = calculate_factorial(num)
	display_result(num, factorial)


def get_user_num() -> int:
	while True:
		try:
			num = int(input('Enter a non-negative integer number: '))
			if num >= 0:
				return num
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a non-negative integer number.\n')


def calculate_factorial(num: int) -> int:
	if num > 0:
		factorial = num

		for i in range(num - 1, 1, -1):
			factorial *= i

	else:
		factorial = 1

	return factorial


def display_result(num: int, factorial: int) -> None:
	print(f'{num}! = {factorial}')


if __name__ == '__main__':
	main()
