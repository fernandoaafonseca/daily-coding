'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 4 and how many end in a 9.
'''


def main():
	squares_ending_in_four, squares_ending_in_nine = count_squares_ending_in_four_and_nine()
	display_result(squares_ending_in_four, squares_ending_in_nine)


def count_squares_ending_in_four_and_nine() -> int:
	ending_in_four = 0
	ending_in_nine = 0

	for num in range(1, 101):
		# For base 10 numbers, num % 10 gives the last digit
		if (num * num) % 10 == 4:
			ending_in_four += 1
		elif (num * num) % 10 == 9:
			ending_in_nine += 1

	return ending_in_four, ending_in_nine


def display_result(squares_ending_in_four: int, squares_ending_in_nine: int) -> None:
	print(f'There are {squares_ending_in_four} squares of the numbers from 1 to 100 ending in 4 and {squares_ending_in_nine} ending in 9.')


if __name__ == '__main__':
	main()