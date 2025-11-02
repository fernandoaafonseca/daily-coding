'''
Write a program that asks the user to enter a number and prints the sum of the divisors of that number. The sum of the divisors of a number is an important function in number theory.
'''


def main():
	number = get_number()
	divisors = get_divisors(number)
	sum_of_all_divisors = calc_sum_all_divisors(divisors)
	display_result(number, sum_of_all_divisors)


def get_number() -> int:
	while True:
		try:
			number = int(input('Enter an integer different than 0: '))
			return number
		except ValueError:
			print('\nPlease enter a valid integer different than 0.\n')


def get_divisors(number: int) -> list[int]:
	divisors = []

	for i in range(1, number + 1):
		if number % i == 0:
			divisors.append(i)

	return divisors


def calc_sum_all_divisors(divisors: list[int]) -> int:
	total_sum = 0

	for i in range(len(divisors)):
		total_sum += divisors[i]

	return total_sum


def display_result(number: int, sum_of_all_divisors: int) -> None:
	print(f'\nThe sum of all divisors of the number {number} is: {sum_of_all_divisors}')


if __name__ == '__main__':
	main()