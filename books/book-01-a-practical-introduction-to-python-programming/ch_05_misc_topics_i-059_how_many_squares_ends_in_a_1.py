'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
'''


def main():
	squares_ending_in_one = count_squares_ending_in_one()
	display_result(squares_ending_in_one)


def count_squares_ending_in_one() -> int:
	counter = 0

	for num in range(1, 101):
		# For base 10 numbers, num % 10 gives the last digit
		if (num * num) % 10 == 1:
			counter += 1

	return counter


def display_result(squares_ending_in_one: int) -> None:
	print(f'There are {squares_ending_in_one} squares of the numbers from 1 to 100 ending in 1.')


if __name__ == '__main__':
	main()