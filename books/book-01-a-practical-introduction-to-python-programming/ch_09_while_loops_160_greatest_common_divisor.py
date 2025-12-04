'''
The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by. For instance, GCD (18, 42) is 6 because the largest number that both 18 and 42 are divisible by is 6. Write a program that asks the user for two numbers and computes their GCD. Shown below is a way to compute the GCD, called Euclid’s Algorithm.

	- First compute the remainder of dividing the larger number by the smaller number.
	- Next, replace the larger number with the smaller number and the smaller number with the remainder.
	- Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.
'''


import os


def main() -> None:
	numbers = get_numbers()
	gcd = find_gcd(numbers)
	display_result(numbers, gcd)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_numbers() -> list[int, int]:
	numbers = []

	while len(numbers) < 2:
		try:
			clear_terminal()
			new_num = int(input('Enter a number: '))

			if new_num > 0:
				numbers.append(new_num)
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a valid integer number.')
			press_any_key_to_continue()

	return numbers



def find_gcd(numbers: list[int]) -> int:
	'''
	Computes the greatest common divisor (GCD) of two integers using
	Euclid's Algorithm. The process repeatedly replaces the larger
	number with the smaller number and the smaller number with the
	remainder until the smaller number becomes zero.
	'''
	larger_num = max(numbers)
	smaller_num = min(numbers)

	while smaller_num != 0:
		remainder = larger_num % smaller_num
		# Update values according to Euclid's Algorithm
		larger_num, smaller_num = smaller_num, remainder

	# larger_num now holds the GCD
	return larger_num


def display_result(numbers: list[int, int], gcd: int) -> None:
	clear_terminal()
	print(f'The GCD of {numbers} is {gcd}')


if __name__ == '__main__':
	main()