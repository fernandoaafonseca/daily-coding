'''
Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.

    *
   * *
  *****
 *     *
*       *
'''


def main() -> None:
	letter_size = get_letter_size()
	print_letter_a(letter_size)


def get_letter_size() -> int:
    while True:
        try:
            letter_size = int(input('Enter how large the letter "A" should be: '))
            if letter_size >= 3:
                return letter_size
        
        except ValueError:
        	print('\nPlease enter a valid integer!')
        print('\nPlease enter an integer greater than or equal to 3!')
        print()


def print_letter_a(letter_size: int) -> None:
	middle_line = letter_size // 2

	for row in range(letter_size):
		# Top rows of the letter A
		if row == 0:
			empty_spaces = letter_size - row - 1
			print(' ' * empty_spaces, end='')
			print('*')
		
		# Middle bar of the letter A
		elif row == middle_line:
			empty_spaces = letter_size - row - 1
			is_letter_size_odd = (letter_size % 2 != 0)
			if is_letter_size_odd:
				asterisks_amount = letter_size
			else:
				asterisks_amount = letter_size + 1

			print(' ' * empty_spaces, end='')

			print('*' * asterisks_amount)

		# Other rows
		else:
			empty_spaces = 2 * row - 1
			print(' ' * (letter_size - row - 1), end='')
			print('*', end='')
			print(' ' * empty_spaces, end='')
			print('*')


if __name__ == '__main__':
	main()