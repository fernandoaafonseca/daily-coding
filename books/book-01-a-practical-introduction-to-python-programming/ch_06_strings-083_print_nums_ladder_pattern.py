'''
Ask the user for a number and then print the following, where the pattern ends at the number that the user enters.

	1
	 2
	  3
	   4
'''


def main() -> None:
	num_lines = get_num()
	print_ladder_pattern(num_lines)


def get_num() -> int:
	while True:
		try:
			num_lines = int(input('Enter how many lines you want to print: '))
			return num_lines
		except ValueError:
			print('\nPlease enter a valid number.\n')


def print_ladder_pattern(num_lines: int) -> None:
	empty_spaces = 0

	print()

	for num in range(num_lines):
		print(' ' * empty_spaces, end='')
		print(num + 1)
		empty_spaces += 1


if __name__ == '__main__':
	main()