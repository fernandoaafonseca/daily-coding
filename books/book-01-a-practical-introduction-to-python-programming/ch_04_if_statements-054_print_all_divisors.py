'''
Write a program that asks the user to enter a number and prints out all the divisors of that number. [Hint: the % operator is used to tell if a number is divisible by something. See Section 3.2.]
'''


def main():
	number = get_number()
	divisors = get_divisors(number)
	display_result(number, divisors)


def get_number() -> int:
	while True:
		try:
			number = int(input('Enter an integer different than 0: '))
			return number
		except ValueError:
			print('Please enter a valid integer different than 0.\n')


def get_divisors(number: int) -> list[int]:
	divisors = []

	for i in range(1, number + 1):
		if number % i == 0:
			divisors.append(i)

	return divisors


def display_result(number: int, divisors: list[int]) -> None:
	print(f'The divisors of {number} are:')

	for i in range(len(divisors) - 1):
		print(f'{divisors[i]}, ', end='')
	print(f'{divisors[-1]}.')


if __name__ == '__main__':
	main()